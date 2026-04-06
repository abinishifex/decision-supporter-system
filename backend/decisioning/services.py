import json
from django.conf import settings
import google.generativeai as genai
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


# ---------------------------------------------------------------------------
# Domain-expert context injected into every AI prompt.
# Each entry: persona, criteria (key eval axes), ethiopia (local context).
# ---------------------------------------------------------------------------
CATEGORY_INSIGHTS = {
    "Career": {
        "persona": "an experienced Ethiopian career counsellor who understands the local job market",
        "criteria": "Ethiopian job market demand, salary vs. job security trade-off, transferable skills, growth trajectory, work-life balance in Ethiopian work culture",
        "ethiopia": "Consider: high graduate unemployment in Ethiopia, prestige of government vs. private sector, informal referral networks (connections) needed for advancement, 2-hour commute reality in Addis Ababa, and salary levels relative to Ethiopian cost of living.",
    },
    "Education": {
        "persona": "a tenured Ethiopian university professor and academic advisor",
        "criteria": "institutional quality and accreditation in Ethiopia, employability post-graduation, family financial burden, scholarship availability, practical vs. theoretical curriculum",
        "ethiopia": "Factor in: EUEE (Ethiopian University Entrance Exam) competition, private vs. public university value, studying abroad vs. local options, family expectation towards STEM/Medicine/Law, and the near-absence of formal student loan systems in Ethiopia.",
    },
    "Business": {
        "persona": "a seasoned Ethiopian entrepreneur and startup advisor who has operated in Addis Ababa",
        "criteria": "access to startup capital in Ethiopia, local market size and competition, import/export regulations, infrastructure constraints, scalability, risk-reward in Ethiopian Birr",
        "ethiopia": "Consider: limited formal funding, reliance on Iqub (rotating savings groups), bureaucratic barriers to business registration, power and internet outage risks, import-driven supply chain costs, and the large untapped youth consumer market in Ethiopia.",
    },
    "Relationships": {
        "persona": "a culturally aware Ethiopian relationship and family counsellor",
        "criteria": "alignment of long-term life goals, family approval (critical in Ethiopian society), emotional safety and mutual respect, financial compatibility, communication style",
        "ethiopia": "Keep in mind: strong expectation of parental and family approval, role of religion (Orthodox, Muslim, Protestant) in relationship choices, bride price (tilosh) considerations, social pressure to marry, build a home, and start a family early in Ethiopian culture.",
    },
    "Family": {
        "persona": "a family systems therapist familiar with Ethiopian multi-generational household dynamics",
        "criteria": "impact on all household members, financial stability of the family unit, balance of cultural duty vs. individual needs, resilience if the decision fails, long-term family harmony",
        "ethiopia": "Consider: extended family financial obligations (supporting parents, funding siblings' education), cultural duties during major holidays (Timkat, Eid, Christmas), the norm of multi-generational households in Ethiopia, and social stigma attached to certain family decisions.",
    },
    "Health": {
        "persona": "an Ethiopian medical professional and public health advisor",
        "criteria": "accessibility (clinics in Addis vs. rural), cost vs. effectiveness, long-term sustainability, physical and mental energy impact, preventive vs. curative approach",
        "ethiopia": "Factor in: Addis-only access to specialists, cost of private vs. public hospitals, role of traditional medicine and herbal remedies, the Ethiopian diet context (mostly plant-based fasting), stigma around mental health treatment, and limited health insurance coverage.",
    },
    "Lifestyle": {
        "persona": "a lifestyle and wellness coach who understands daily life in urban Ethiopia",
        "criteria": "daily quality of life within Ethiopian income reality, financial sustainability, social acceptance, long-term personal fulfilment, impact on family responsibilities",
        "ethiopia": "Consider: rising rent and transport costs in Addis Ababa, social judgment from neighbours and relatives, value placed on modesty and community over individual expression, and the joy of communal activities like coffee ceremonies, church, and market days.",
    },
    "Technology": {
        "persona": "a tech entrepreneur and digital consultant familiar with the Ethiopian startup ecosystem",
        "criteria": "reliability given Ethiopia's internet/power infrastructure, cost in ETB, learning curve, local support and maintenance availability, data privacy constraints, productivity gain",
        "ethiopia": "Consider: frequent electricity and internet outages, Ethio Telecom dominance, no access to Stripe/PayPal, growth of local fintech (Telebirr, CBE Birr), and the tech-savvy youth population in Addis, Hawassa, and Dire Dawa.",
    },
    "Personal Growth": {
        "persona": "a life coach and motivational advisor who works with Ethiopian youth and young professionals",
        "criteria": "alignment with personal values and identity, cost and time investment vs. available income, social support system, measurability of progress, impact on family financial obligations",
        "ethiopia": "Consider: pressure to contribute family income early rather than invest in self, limited Amharic self-help resources, faith/church communities as growth networks, mentorship scarcity in Ethiopia, and the expectation to 'give back' to family once you succeed.",
    },
}

DEFAULT_INSIGHT = {
    "persona": "an expert decision-making consultant familiar with Ethiopian society and culture",
    "criteria": "short and long-term consequences, financial feasibility in Ethiopia, impact on family and community, personal values alignment",
    "ethiopia": "Anchor every question in Ethiopian realities: family obligations, limited financial safety nets, cultural community expectations, and infrastructure constraints.",
}


# ---------------------------------------------------------------------------
# Fallback questions used when Gemini quota is exceeded.
# Questions use {A} / {B} / {C} placeholders replaced at runtime.
# ---------------------------------------------------------------------------
FALLBACK_QUESTIONS = {
    "Career": [
        "Which option offers a stronger position in the Ethiopian job market within the next 3 years?",
        "Which option provides better job security given the Ethiopian economic climate?",
        "Which option allows you to build more transferable skills valued by Ethiopian employers?",
        "Which option aligns better with the salary expectations needed to live comfortably in Addis Ababa?",
        "Which option is more likely to advance through informal networks and connections (referrals) in Ethiopia?",
        "Which option offers better work-life balance given typical Ethiopian working hours and commute?",
    ],
    "Education": [
        "Which option is more likely to secure you employment after graduation in Ethiopia?",
        "Which option places a lower financial burden on your family given the cost of education in Ethiopia?",
        "Which option has stronger accreditation and recognition by Ethiopian employers and institutions?",
        "Which option gives you better access to scholarships or financial support in Ethiopia?",
        "Which option provides a more practical, skills-based curriculum relevant to the Ethiopian job market?",
        "Which option better aligns with the STEM-focused expectations of Ethiopian families?",
    ],
    "Business": [
        "Which option requires lower startup capital, considering the limited formal funding in Ethiopia?",
        "Which option is more feasible to fund through Iqub (rotating savings) or family contributions?",
        "Which option is better able to survive frequent power and internet outages in Ethiopia?",
        "Which option has lower exposure to import costs and foreign currency risks in Ethiopia?",
        "Which option has a clearer path to profitability within the Ethiopian market?",
        "Which option faces fewer bureaucratic barriers to registration and operation in Ethiopia?",
    ],
    "Relationships": [
        "Which option is more likely to receive approval from your family and community in Ethiopia?",
        "Which option better aligns with your core values and religious beliefs?",
        "Which option provides greater emotional safety and mutual respect in the long term?",
        "Which option is more compatible with the financial realities of building a home in Ethiopia?",
        "Which option aligns better with your shared long-term life goals?",
        "Which option is most consistent with your communication style and expectations?",
    ],
    "Family": [
        "Which option has a more positive long-term impact on the well-being of all family members?",
        "Which option better respects your extended family obligations (parents, siblings) in Ethiopia?",
        "Which option is more financially sustainable for your household's current income level?",
        "Which option best preserves harmony within your multi-generational family setting?",
        "Which option can your family recover from more easily if things don't go as planned?",
        "Which option is more aligned with your cultural and religious duties as an Ethiopian family?",
    ],
    "Health": [
        "Which option is more accessible and affordable within the Ethiopian public/private health system?",
        "Which option offers a more sustainable long-term approach to your health?",
        "Which option has fewer negative side effects within the Ethiopian healthcare context?",
        "Which option is more compatible with a traditional Ethiopian diet and lifestyle?",
        "Which option reduces your long-term dependency on expensive private hospital visits?",
        "Which option is less likely to carry social stigma in your community?",
    ],
    "Lifestyle": [
        "Which option is more financially sustainable on a typical Ethiopian income in Addis Ababa?",
        "Which option is better accepted by your community and relatives without causing judgment?",
        "Which option allows you to maintain your family responsibilities while pursuing personal goals?",
        "Which option contributes more to your long-term personal fulfilment and happiness?",
        "Which option is more compatible with the rising cost of living in Addis Ababa?",
        "Which option allows you to stay connected to community values like coffee ceremonies and religious events?",
    ],
    "Technology": [
        "Which option works more reliably given Ethiopia's frequent power and internet outages?",
        "Which option is more cost-effective in Ethiopian Birr (ETB) for your budget?",
        "Which option has better local technical support available in Ethiopia?",
        "Which option integrates better with local payment systems like Telebirr or CBE Birr?",
        "Which option has a shorter learning curve for users with limited tech experience?",
        "Which option offers greater productivity gains for your specific work or study context?",
    ],
    "Personal Growth": [
        "Which option better aligns with your personal values and sense of identity?",
        "Which option is more achievable given your current income and time constraints in Ethiopia?",
        "Which option is more likely to be supported by your faith community or social network?",
        "Which option allows you to grow while still meeting your family's financial expectations?",
        "Which option offers more measurable progress that you can track and celebrate?",
        "Which option positions you better to give back to your family and community once you succeed?",
    ],
}

DEFAULT_FALLBACK = [
    "Which option is more financially feasible given your current situation in Ethiopia?",
    "Which option has a more positive impact on your family and community?",
    "Which option aligns better with your personal values and long-term goals?",
    "Which option offers a clearer path forward with fewer major risks?",
    "Which option would you be more comfortable defending to your family and close friends?",
    "Which option are you more likely to be satisfied with 3 years from now?",
]


def _build_fallback_questions(category_name, options):
    """Build structured fallback questions using the pre-written bank."""
    texts = FALLBACK_QUESTIONS.get(category_name, DEFAULT_FALLBACK)
    # Build answer choices dynamically from the user's actual options
    answer_choices = [
        {"label": opt, "value": chr(65 + i)} for i, opt in enumerate(options)
    ]
    return [
        {"id": i + 1, "text": text, "options": answer_choices}
        for i, text in enumerate(texts)
    ]


def generate_dynamic_questions(problem, options, category_name="General"):
    """
    Role 4: Dynamic Question Generation.
    Gemini generates 5-10 domain-specific, Ethiopia-aware questions.
    """
    if not gemini_model:
        raise ValueError("Gemini AI is not configured. Cannot generate dynamic questions.")

    insight = CATEGORY_INSIGHTS.get(category_name, DEFAULT_INSIGHT)
    persona = insight["persona"]
    criteria = insight["criteria"]
    ethiopia = insight["ethiopia"]

    options_str = ", ".join(options)

    prompt = f"""
    You are {persona}.
    A user in Ethiopia is trying to decide between: {options_str}.
    Their problem is: "{problem}"

    Your task is to generate 5 to 8 sharp, investigative, multiple-choice questions that reveal
    which option is the best fit for this specific user.

    DOMAIN FOCUS — your questions MUST probe these specific criteria:
    {criteria}

    ETHIOPIAN CONTEXT — ground every question in this reality:
    {ethiopia}

    STRICT RULES:
    - Each question must be comparative: ask which of the provided options is better for a specific concern.
    - Do NOT ask generic well-being questions like "which option feels healthier" or "which reduces stress".
    - Use EXACTLY these options as the answer choices for every question: {options_str}.
    - Assign letter codes: A = first option, B = second option, C = third (if any), etc.
    - Total questions: between 5 and 8.

    Return ONLY a valid JSON list with this exact structure (no markdown, no explanation):
    [
      {{
        "id": 1,
        "text": "Which option offers a stronger position in the Ethiopian job market within the next 3 years?",
        "options": [
          {{ "label": "{options[0]}", "value": "A" }},
          {{ "label": "{options[1] if len(options) > 1 else options[0]}", "value": "B" }}
        ]
      }}
    ]
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
        err = str(e)
        # On quota exhaustion (429), fall back gracefully instead of crashing
        if "429" in err or "quota" in err.lower() or "rate" in err.lower():
            return _build_fallback_questions(category_name, options)
        raise Exception(f"AI Question Generation failed: {err}")


def _tally_evaluate(options, answers):
    """
    Fallback evaluator: counts how many times each option was picked
    and converts that to 0-100 scores.
    """
    # Build letter → option name map (A→options[0], B→options[1], ...)
    letter_map = {chr(65 + i): opt for i, opt in enumerate(options)}

    # Count votes per option
    counts = {opt: 0 for opt in options}
    for answer_value in answers.values():
        option_name = letter_map.get(str(answer_value).upper())
        if option_name:
            counts[option_name] += 1

    total_answers = sum(counts.values()) or 1  # avoid divide-by-zero

    # Convert to 0-100 scores (round to nearest integer)
    results = sorted(
        [{"name": opt, "score": round((count / total_answers) * 100)}
         for opt, count in counts.items()],
        key=lambda r: r["score"],
        reverse=True,
    )

    winner = results[0]["name"]
    summary = (
        f"Based on your answers, \u201c{winner}\u201d was selected as the best option "
        f"{counts[winner]} out of {total_answers} times across all evaluation criteria. "
        f"This score-based summary was generated automatically because the AI analysis "
        f"quota is temporarily exhausted. The ranking reflects which option you consistently "
        f"preferred when evaluating each criterion. Consider revisiting with Gemini AI "
        f"tomorrow for a deeper qualitative analysis."
    )
    return {"recommendedOption": winner, "results": results, "summary": summary}


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
    
    User Answers:
    {json.dumps(answers, indent=2)}
    
    (Note: Each answer value (A, B, C...) corresponds to an option from the original list.)
    
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
        
        data = json.loads(text)
        # Ensure pros and cons exist for the new schema
        if "pros" not in data:
            data["pros"] = "Pros are subjective and depend on priority."
        if "cons" not in data:
            data["cons"] = "Consider trade-offs."
            
        return data
    except Exception as e:
        err = str(e)
        # On quota exhaustion (429), fall back to tally-based scoring
        if "429" in err or "quota" in err.lower() or "rate" in err.lower():
            fallback_data = _tally_evaluate(options, answers)
            fallback_data["pros"] = "Fallback pros: Consistently chosen."
            fallback_data["cons"] = "Fallback cons: Limited nuance."
            return fallback_data
        raise Exception(f"AI Decision Evaluation failed: {err}")

def validate_decision_payload(data):
    required = ["problem", "options"]
    if not all(k in data for k in required):
        pass
    return data
