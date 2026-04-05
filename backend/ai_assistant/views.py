from django.shortcuts import render

# Create your views here.
from google import genai
import os
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .serializers import DecisionStartSerializer
import json

load_dotenv(os.path.join(os.path.dirname(__file__), '../..', '.env'))

os.environ['GOOGLE_API_KEY'] = os.getenv('GEMINI_API_KEY')

client = genai.Client()

@csrf_exempt
def test_view(request):
    return JsonResponse({"test": "ok"})

@csrf_exempt
def start_decision(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    serializer = DecisionStartSerializer(data=data)
    if not serializer.is_valid():
        return JsonResponse({"error": serializer.errors}, status=400)

    problem = serializer.validated_data['problem']
    options = serializer.validated_data['options']

    ai_response = gemini_decision(problem, options)
    print(ai_response)

    try:
        ai_data = json.loads(ai_response)
    except:
        ai_data = {"error": ai_response}

    return JsonResponse({
        "problem": problem,
        "options": options,
        "ai_result": ai_data
    })

def gemini_decision(problem, options):
    try:
        prompt = f"""
        Return ONLY valid JSON.

        Problem: {problem}
        Options: {options}

        Format:
        {{
          "recommended_option": "one option exactly",
          "reason": "short explanation"
        }}
        """

        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        # Fallback: Simple rule-based recommendation
        return simple_ai_recommendation(problem, options)

def simple_ai_recommendation(problem, options):
    # Simple AI: Analyze keywords in problem and options
    problem_lower = problem.lower()
    
    # Define some simple rules
    if 'buy' in problem_lower or 'purchase' in problem_lower:
        if 'new' in problem_lower:
            reason = "New purchases often provide better value and features"
        else:
            reason = "Consider the cost-benefit of buying vs alternatives"
    elif 'keep' in problem_lower or 'maintain' in problem_lower:
        reason = "Maintaining current situation avoids change and risk"
    elif 'change' in problem_lower or 'switch' in problem_lower:
        reason = "Change can bring new opportunities but involves risk"
    else:
        reason = "Based on general decision-making principles"
    
    # Recommend first option as default
    recommended = options[0]
    
    # Simple preference: prefer options with positive words
    positive_words = ['new', 'better', 'improved', 'modern', 'efficient']
    for option in options:
        if any(word in option.lower() for word in positive_words):
            recommended = option
            reason += f", favoring '{option}' due to positive attributes"
            break
    
    return f'{{"recommended_option": "{recommended}", "reason": "{reason}"}}'