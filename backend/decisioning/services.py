def evaluate_dynamic_decision(problem, category, options, answers):
    """
    Step 2: Analyzes the options based on the user's answers.
    """
    # Simulate scoring logic
    results = [{"name": opt, "score": 85, "percentage": 85.0} for opt in options]
    recommended = options[0] if options else None
    
    # NEW: Logic to create split analysis instead of one string
    summary = f"Based on your criteria for '{problem}', {recommended} is the strongest choice."
    pros = f"This option aligns best with your goals in the {category.get('name', 'selected')} category."
    cons = "Some trade-offs may exist regarding secondary priorities."

    return {
        "results": results,
        "recommendedOption": recommended,
        "summary": summary, # Matches views.py evaluation.get("summary")
        "pros": pros,       # Matches views.py evaluation.get("pros")
        "cons": cons        # Matches views.py evaluation.get("cons")
    }

# Keep the others as they were or update as needed
def generate_dynamic_questions(problem, category):
    return {
        "questions": [
            {"id": "q1", "text": f"How important is cost for this {category.get('name')}?"},
            {"id": "q2", "text": "What is your primary goal?"}
        ]
    }

def validate_decision_payload(data):
    required = ["problem", "category", "options", "answers"]
    if not all(k in data for k in data):
        # You can add more specific validation here if needed
        pass
    return data