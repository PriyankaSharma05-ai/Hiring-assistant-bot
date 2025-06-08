def get_prompt_for_info(user_input):
    return f"You are an HR assistant. Ask the candidate for their full name, email, phone number, experience, location, desired position, and tech stack."

def get_questions_prompt(tech_stack_input):
    return f"Generate 3-5 technical questions for an applicant skilled in: {tech_stack_input}."
