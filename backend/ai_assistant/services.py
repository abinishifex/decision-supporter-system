from django.conf import settings

try:
    from groq import Groq
    groq_client = Groq(api_key=settings.GROQ_API_KEY) if getattr(settings, "GROQ_API_KEY", None) else None
except ImportError:
    groq_client = None


def build_chat_response(message):
    if not groq_client:
        return "Groq AI is not currently configured. Please check your API key."

    system_prompt = (
        "You are a helpful 'Decision Coach' for a web application that helps people "
        "make complex choices. Users input a problem, options, and rate them across "
        "categories. Keep your answers concise, friendly, and practical. "
        "Do not use complex markdown."
    )

    try:
        completion = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message},
            ],
            temperature=0.7,
            max_tokens=250,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Sorry, the AI is momentarily unavailable. (Error: {str(e)})"
