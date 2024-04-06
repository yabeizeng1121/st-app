import streamlit as st
from utils.chatbot import get_chatbot_response
import json


def load_streamlit_updates():
    try:
        with open("data/streamlit_updates.json", "r") as file:
            updates = json.load(file)
        return updates
    except Exception as e:
        st.error(f"Failed to load updates: {e}")
        return {}


def main():
    st.set_page_config(
        page_title="Streamlit Chatbot", layout="wide", initial_sidebar_state="expanded"
    )

    # Custom CSS to emulate the design from the provided image
    st.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                background-image: linear-gradient(#2e7bcf,#2e7bcf);
                color: white;
            }
            .block-container {
                padding-top: 5rem;
                padding-bottom: 5rem;
            }
            h1 {
                color: white;
            }
            .css-1d391kg {
                padding-top: 5rem;
                padding-bottom: 5rem;
            }
        </style>
    """,
        unsafe_allow_html=True,
    )

    # Load updates and handle chat
    updates = load_streamlit_updates()

    # Sidebar
    with st.sidebar:
        st.image("assets/images/logo.png", width=100)
        st.header("Streamlit Chatbot")
        Answer = st.radio(
            "Do you like this Chatbot?",
            [
                "Yes! :100:",
                "Needs Improvement :point_up_2:",
                "No Comments :female-technologist:",
            ],
            index=None,
        )

        st.write("You selected:", Answer)
        st.markdown("---")
        st.markdown("Show Basic Interactions")

    st.title("Streamlit Chatbot")

    user_input = st.text_input("Ask me anything:")
    if user_input:
        response = get_chatbot_response(user_input)  # Integrate update retrieval here
        st.write(response)


if __name__ == "__main__":
    main()
