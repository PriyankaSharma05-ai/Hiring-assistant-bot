from prompts import get_prompt_for_info, get_questions_prompt
from utils import call_llm, detect_exit

def run_chatbot(user_input, chat_history):
    if detect_exit(user_input):
        return "Thank you for your time. We will be in touch soon!"
    
    if "tech stack" in user_input.lower():
        tech_prompt = get_questions_prompt(user_input)
        return call_llm(tech_prompt)
    
    info_prompt = get_prompt_for_info(user_input)
    return call_llm(info_prompt)

