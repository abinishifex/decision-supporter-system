from statistics import mean
from django.conf import settings

try:
    from groq import Groq
    groq_client = Groq(api_key=settings.GROQ_API_KEY) if getattr(settings, "GROQ_API_KEY", None) else None
except ImportError:
    groq_client = None



def build_strengths(category, option_answers):
    strengths = []
    for question in category.questions.prefetch_related('options'):
        selected_value = option_answers[str(question.id)]
        selected_option = next(
            (opt for opt in question.options.all() if opt.value == selected_value),
            None,
        )
        strengths.append(
            {
                "questionId": question.id,
                "question": question.text,
                "value": selected_value,
                "label": selected_option.label if selected_option else str(selected_value),
            }
        )
    strengths.sort(key=lambda item: item["value"], reverse=True)
    return strengths


def build_analysis(problem, category, ranked_results):
    winner = ranked_results[0]
    rest = ranked_results[1:]
    margin = winner["score"] - rest[0]["score"] if rest else 0
    average_score = mean(result["score"] for result in ranked_results)
    strengths = ", ".join(item["question"] for item in winner["topStrengths"])

    if margin >= 4:
        edge = "a clear lead"
    elif margin >= 2:
        edge = "a moderate lead"
    else:
        edge = "a narrow lead"

    fallback = (
        f"For '{problem}', {winner['name']} finished with {edge} in the {category.name} category. "
        f"It stood out most on {strengths}. The option scored {winner['score']} compared with a session average "
        f"of {average_score:.1f}, which indicates stronger alignment with the criteria you rated."
    )

    if not groq_client:
        return fallback

    prompt = f"""
You are an expert decision-making coach. The user is deciding on: "{problem}".
They evaluated options using the "{category.name}" framework.
The top recommended option is "{winner['name']}" with a score of {winner['score']}.
The average score was {average_score:.1f}.
The top strengths of the winning option are: {strengths}.

Write a concise, 1-2 paragraph analytical and encouraging summary explaining why {winner['name']} is the best choice based on these strengths. Do not mention that a user 'rated' these, just frame them as the objective strengths of the option. Do not use markdown blocks.
"""
    try:
        completion = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return fallback


def evaluate_decision(problem, category, options, answers):
    # Calculate accurate max score dynamically by finding the highest rated answer for each question
    max_score = sum(max((opt.value for opt in q.options.all()), default=0) for q in category.questions.prefetch_related('options'))
    if max_score == 0:
        max_score = 1

    results = []

    for index, option_name in enumerate(options):
        option_answers = answers[str(index)]
        score = sum(option_answers.values())
        strengths = build_strengths(category, option_answers)
        results.append(
            {
                "name": option_name,
                "score": score,
                "percentage": round((score / max_score) * 100, 2),
                "topStrengths": strengths[:3],
            }
        )

    results.sort(key=lambda item: (-item["score"], item["name"].lower()))
    analysis = build_analysis(problem, category, results)

    return {
        "category": {"id": category.id, "name": category.name},
        "maxScore": max_score,
        "recommendedOption": results[0]["name"],
        "results": results,
        "analysis": analysis,
    }
