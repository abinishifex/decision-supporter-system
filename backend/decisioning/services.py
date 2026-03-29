from statistics import mean


def validate_category(category):
    if not isinstance(category, dict):
        raise ValueError("Category payload must be an object.")

    category_id = str(category.get("id", "")).strip()
    category_name = str(category.get("name", "")).strip()
    questions = category.get("questions", [])

    if not category_id or not category_name:
        raise ValueError("Category id and name are required.")
    if not isinstance(questions, list) or not questions:
        raise ValueError("Category must include at least one question.")

    normalized_questions = []
    for question in questions:
        if not isinstance(question, dict):
            raise ValueError("Each question must be an object.")

        question_id = str(question.get("id", "")).strip()
        question_text = str(question.get("text", "")).strip()
        options = question.get("options", [])

        if not question_id or not question_text:
            raise ValueError("Each question must include an id and text.")
        if not isinstance(options, list) or not options:
            raise ValueError(f"Question {question_id} must include answer options.")

        normalized_options = []
        for option in options:
            if not isinstance(option, dict):
                raise ValueError(f"Question {question_id} contains an invalid option.")
            label = str(option.get("label", "")).strip()
            try:
                value = int(option.get("value"))
            except (TypeError, ValueError):
                raise ValueError(f"Question {question_id} has a non-numeric option value.")
            if not label:
                raise ValueError(f"Question {question_id} contains an unlabeled option.")
            normalized_options.append({"label": label, "value": value})

        normalized_questions.append(
            {"id": question_id, "text": question_text, "options": normalized_options}
        )

    return {
        "id": category_id,
        "name": category_name,
        "description": str(category.get("description", "")).strip(),
        "icon": str(category.get("icon", "")).strip(),
        "questions": normalized_questions,
    }


def validate_decision_payload(payload):
    if not isinstance(payload, dict):
        raise ValueError("Request body must be a JSON object.")

    problem = str(payload.get("problem", "")).strip()
    if len(problem) < 6:
        raise ValueError("Problem statement must be at least 6 characters long.")

    raw_options = payload.get("options", [])
    if not isinstance(raw_options, list) or len(raw_options) < 2:
        raise ValueError("At least two options are required.")

    options = [str(option).strip() for option in raw_options]
    if any(not option for option in options):
        raise ValueError("Option names cannot be empty.")

    category = validate_category(payload.get("category"))
    raw_answers = payload.get("answers", {})
    if not isinstance(raw_answers, dict):
        raise ValueError("Answers must be an object keyed by option index.")

    valid_values = {
        question["id"]: {int(option["value"]) for option in question["options"]}
        for question in category["questions"]
    }
    question_ids = [question["id"] for question in category["questions"]]

    normalized_answers = {}
    for option_index in range(len(options)):
        option_key = str(option_index)
        option_answers = raw_answers.get(option_key, raw_answers.get(option_index))
        if not isinstance(option_answers, dict):
            raise ValueError(f"Missing answers for option {option_index + 1}.")

        normalized_option = {}
        for question_id in question_ids:
            raw_value = option_answers.get(question_id, option_answers.get(int(question_id) if str(question_id).isdigit() else question_id))
            if raw_value is None:
                raise ValueError(f"Question {question_id} is unanswered for option {option_index + 1}.")
            try:
                value = int(raw_value)
            except (TypeError, ValueError):
                raise ValueError(f"Question {question_id} has an invalid answer value.")
            if value not in valid_values[question_id]:
                raise ValueError(f"Question {question_id} has an unsupported answer value.")
            normalized_option[question_id] = value

        normalized_answers[option_key] = normalized_option

    return {
        "problem": problem,
        "category": category,
        "options": options,
        "answers": normalized_answers,
    }


def build_strengths(category, option_answers):
    strengths = []
    for question in category["questions"]:
        selected_value = option_answers[question["id"]]
        selected_option = next(
            (option for option in question["options"] if option["value"] == selected_value),
            None,
        )
        strengths.append(
            {
                "questionId": question["id"],
                "question": question["text"],
                "value": selected_value,
                "label": selected_option["label"] if selected_option else str(selected_value),
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

    return (
        f"For '{problem}', {winner['name']} finished with {edge} in the {category['name']} category. "
        f"It stood out most on {strengths}. The option scored {winner['score']} compared with a session average "
        f"of {average_score:.1f}, which indicates stronger alignment with the criteria you rated."
    )


def evaluate_decision(problem, category, options, answers):
    max_score = max(option["value"] for question in category["questions"] for option in question["options"])
    max_score *= len(category["questions"])
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
        "category": {"id": category["id"], "name": category["name"]},
        "maxScore": max_score,
        "recommendedOption": results[0]["name"],
        "results": results,
        "analysis": analysis,
    }


def build_chat_response(message):
    lowered = message.lower()

    if any(word in lowered for word in ["category", "categories"]):
        return "Choose the category that best matches the type of decision you are making, then answer every question for each option."
    if any(word in lowered for word in ["score", "rank", "result", "recommend"]):
        return "Scores are calculated by summing the values for each answer. The highest total becomes the recommended option."
    if any(word in lowered for word in ["start", "how", "use", "help"]):
        return "Start on the decision page, describe the problem, list your options, pick a category, answer the questions, and review the recommendation."

    return "I can explain the workflow, how scoring works, or how to frame your options more clearly."
