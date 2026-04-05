import json
from django.conf import settings
import google.generativeai as genai

try:
    if getattr(settings, "GEMINI_API_KEY", None):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        # Use the explicit model paths for SDK 0.8.3 stability
        gemini_model = genai.GenerativeModel("models/gemini-2.5-flash")
    else:
        gemini_model = None
except Exception:
    gemini_model = None


def generate_dynamic_questions(problem, options, category_name="General"):
    """
    Role 4: Dynamic Question Generation.
    Gemini generates 5-10 tailored questions based on the problem, options, and category.
    """
    if not gemini_model:
        raise ValueError("Gemini AI is not configured. Cannot generate dynamic questions.")

    prompt = f"""
    You are a decision-making psychologist specializing in {category_name}.
    The user is deciding between these options: {options}.
    The problem statement is: "{problem}".

    Generate 5 to 10 investigative multiple-choice questions that help the user clarify their priorities.
    Guidelines:
    - Use THESE original options as the only multiple-choice answers for EVERY question: {options}.
    - The "options" object in your JSON response MUST contain ALL {len(options)} options provided in the list above.
    - Assign each option a letter (A, B, C, D, E) based on its order in the list.
    - Each question should ask which option (A, B, C...) best satisfies a certain priority, concern, or long-term goal.
    
    Return ONLY a JSON list of objects with the following structure:
    [
      {{
        "id": 1,
        "text": "Which option offers better [Factor]?",
        "options": {{
          "A": "Option 1 Name",
          "B": "Option 2 Name",
          "...": "..." 
        }}
      }}
    ]
    Do not add any "Custom" or "Other" options.
    Do not use markdown formatting or code blocks.
    """

    try:
        response = gemini_model.generate_content(prompt)
        text = response.text.strip()
        # Remove any potential markdown blocks
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:].strip()
        
        questions = json.loads(text)
        return questions
    except Exception as e:
        raise Exception(f"AI Question Generation failed: {str(e)}")


def evaluate_dynamic_decision(problem, options, questions, answers):
    """
    Role 4: Dynamic Evaluation.
    Gemini analyzes the answers and provides a weighted result based on original options.
    """
    if not gemini_model:
        raise ValueError("Gemini AI is not configured. Cannot evaluate.")

    # Prepare context for Gemini
    # answers is a dict: { "question_id": "A/B/C/..." }
    
    prompt = f"""
    Evaluate the following decision problem: "{problem}"
    Options to compare: {options}
    
    The user answered these investigative questions:
    {json.dumps(questions, indent=2)}
    
    User Answers (per option):
    {json.dumps(answers, indent=2)}
    
    Your Task:
    1. Perform a weighted analysis. Determine which option is the winner.
    2. Provide a score (0-100) for each option.
    3. Return a JSON object with:
       - "recommendedOption": The name of the winning option.
       - "results": A list of {{ "name": "Option Name", "score": 85 }} objects.
        - "summary": A 1-2 paragraph overview of the decision.
    Do not use markdown formatting or code blocks.
    """

    try:
        response = gemini_model.generate_content(prompt)
        text = response.text.strip()
        # Remove any potential markdown blocks
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:].strip()
        
        return json.loads(text)
    except Exception as e:
        raise Exception(f"AI Decision Evaluation failed: {str(e)}")
