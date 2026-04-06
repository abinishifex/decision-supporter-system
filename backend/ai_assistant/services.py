from django.conf import settings

import google.generativeai as genai

try:
    if getattr(settings, "GEMINI_API_KEY", None):
        genai.configure(api_key=settings.GEMINI_API_KEY)
    else:
        pass
except ImportError:
    pass


def build_chat_response(message, history=None):
    if not getattr(settings, "GEMINI_API_KEY", None):
        return "Gemini AI is not currently configured. Please check your API key."

    system_prompt = (
        "You are a helpful 'Decision Coach' for a web application that helps people "
        "make complex choices. Users input a problem, options, and rate them across "
        "categories. Keep your answers concise, friendly, and practical. "
        "Do not use complex markdown."
    )

    # Format history for Gemini API
    gemini_history = []
    if history:
        for msg in history:
            role = "user" if msg.get("sender") == "user" else "model"
            parts = str(msg.get("text", ""))
            
            # Gemini strictly forbids the very first message in history from being a "model" message. 
            # Our frontend defaults the first message to a bot greeting, we skip it.
            if len(gemini_history) == 0 and role == "model":
                continue
                
            gemini_history.append({"role": role, "parts": parts})

    try:
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=system_prompt
        )
        
        chat = model.start_chat(history=gemini_history)
        response = chat.send_message(message)
        return response.text.strip()
    except Exception as e:
        return f"Sorry, the AI is momentarily unavailable. (Error: {str(e)})"
