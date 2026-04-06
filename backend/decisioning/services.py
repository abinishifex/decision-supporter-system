def validate_category(category):
    if not isinstance(category, dict):
        raise ValueError("Category is required.")

    category_id = str(category.get("id") or "").strip()
    category_name = str(category.get("name") or "").strip()
    questions = category.get("questions")

    if not category_id or not category_name:
        raise ValueError("Category id and name are required.")
    if not isinstance(questions, list) or not questions:
        raise ValueError("Category questions are required.")

    normalized_questions = []
    for question in questions:
        question_id = str(question.get("id") or "").strip()
        question_text = str(question.get("text") or "").strip()
        options = question.get("options")

        if not question_id or not question_text:
            raise ValueError("Every question must include id and text.")
        if not isinstance(options, list) or not options:
            raise ValueError("Every question must include answer options.")

        allowed_values = []
        normalized_options = []
        for option in options:
            label = str(option.get("label") or "").strip()
            value = option.get("value")
            if not label or not isinstance(value, int):
                raise ValueError("Every answer option must include label and integer value.")
            allowed_values.append(value)
            normalized_options.append({"label": label, "value": value})

        normalized_questions.append(
            {
                "id": question_id,
                "text": question_text,
                "options": normalized_options,
                "allowedValues": allowed_values,
            }
        )

    return {
        "id": category_id,
        "name": category_name,
        "questions": normalized_questions,
    }


def validate_decision_payload(payload):
    if not isinstance(payload, dict):
        raise ValueError("Invalid request payload.")

    problem = str(payload.get("problem") or "").strip()
    options = payload.get("options")
    category = validate_category(payload.get("category"))
    answers = payload.get("answers")

    if len(problem) < 5:
        raise ValueError("Problem statement must be at least 5 characters.")
    if not isinstance(options, list):
        raise ValueError("Options are required.")

    normalized_options = [str(option).strip() for option in options if str(option).strip()]
    if len(normalized_options) < 2:
        raise ValueError("At least two options are required.")
    if len(normalized_options) != len(options):
        raise ValueError("Option names cannot be empty.")

    if not isinstance(answers, dict):
        raise ValueError("Answers are required.")

    normalized_answers = {}
    questions_by_id = {question["id"]: question for question in category["questions"]}

    for option_index in range(len(normalized_options)):
        option_key = str(option_index)
        option_answers = answers.get(option_key, answers.get(option_index))
        if not isinstance(option_answers, dict):
            raise ValueError(f"Answers are required for option {option_index + 1}.")

        normalized_option_answers = {}
        for question in category["questions"]:
            question_key = question["id"]
            raw_value = option_answers.get(question_key)
            if raw_value is None and question_key.isdigit():
                raw_value = option_answers.get(int(question_key))
            if not isinstance(raw_value, int):
                raise ValueError(f"Answer missing for question {question['text']}.")
            if raw_value not in questions_by_id[question_key]["allowedValues"]:
                raise ValueError(f"Invalid answer value for question {question['text']}.")
            normalized_option_answers[question_key] = raw_value

        normalized_answers[option_key] = normalized_option_answers

    return {
        "problem": problem,
        "options": normalized_options,
        "category": category,
        "answers": normalized_answers,
    }


def build_strengths(category, option_answers):
    strengths = []
    for question in category["questions"]:
        value = option_answers.get(question["id"])
        if value == max(question["allowedValues"]):
            strengths.append(question["text"])
    return strengths[:3]


def build_analysis(problem, category, ranked_results):
    top = ranked_results[0]
    runner_up = ranked_results[1] if len(ranked_results) > 1 else None

    if runner_up:
        margin = top["score"] - runner_up["score"]
        return (
            f'For "{problem}", {top["name"]} scored highest in the {category["name"]} category. '
            f'It finished {margin} point{"s" if margin != 1 else ""} ahead of {runner_up["name"]} '
            f'and showed the strongest overall fit across the selected questions.'
        )

    return (
        f'For "{problem}", {top["name"]} is the recommended choice in the {category["name"]} category '
        "based on the submitted answers."
    )


def evaluate_decision(problem, category, options, answers):
    max_score = sum(max(question["allowedValues"]) for question in category["questions"])
    results = []

    for index, option_name in enumerate(options):
        option_answers = answers[str(index)]
        score = sum(option_answers.values())
        percentage = round((score / max_score) * 100, 2) if max_score else 0
        results.append(
            {
                "name": option_name,
                "score": score,
                "percentage": percentage,
                "strengths": build_strengths(category, option_answers),
            }
        )

    ranked_results = sorted(results, key=lambda item: item["score"], reverse=True)
    analysis = build_analysis(problem, category, ranked_results)

    return {
        "results": ranked_results,
        "analysis": analysis,
        "maxScore": max_score,
        "recommendedOption": ranked_results[0]["name"],
    }


def build_chat_response(message):
    text = (message or "").strip().lower()
    if not text:
        return "Please send a message so I can help."
    if "hello" in text or "hi" in text:
        return "Hello. Share your decision and I can help you think through it."
    if "career" in text or "job" in text:
        return "For career decisions, compare growth, compensation, stability, and work-life balance."
    if "money" in text or "finance" in text or "invest" in text:
        return "For finance decisions, weigh return potential, risk, liquidity, and time horizon."
    if "health" in text:
        return "For health decisions, focus on safety, sustainability, cost, and long-term benefit."
    return "List your options clearly, choose the closest category, and answer each question consistently."

