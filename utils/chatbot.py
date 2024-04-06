from transformers import pipeline, Conversation


def get_chatbot_response(user_input):
    chatbot = pipeline("conversational", model="microsoft/DialoGPT-large")
    conversation = Conversation(user_input)
    chatbot(conversation)
    return conversation.generated_responses[-1]
