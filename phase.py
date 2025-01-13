
# Phase 1 libraries
import warnings
import logging
from dotenv import load_dotenv


import streamlit as st

# Phase 2 libraries
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

# Disable warnings and info logs
warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)

# Fetch API key from the environment variable
api_key = os.getenv("GROQ_API_Key")
if not api_key:
    raise ValueError("GROQ_API_Key is not set in the .env file or environment variables.")

# Phase 2: Streamlit UI
st.title("Ask Chatbot!")
st.markdown("This chatbot uses a RAG-based model to answer queries accurately and contextually.")

# Setup a session state variable to hold all the old messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display all the historical messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])


prompt = st.chat_input('Pass your prompt here')

if prompt:
    st.chat_message('user').markdown(prompt)
    # Store the user prompt in state
    st.session_state.messages.append({'role':'user', 'content': prompt})
    
    # Phase 2 
    groq_sys_prompt = ChatPromptTemplate.from_template("""You are very smart at everything, you always give the best, 
                                            the most accurate and most precise answers. Answer the following Question: {user_prompt}.
                                            Start the answer directly. No small talk please""")

    #model = "mixtral-8x7b-32768"
    model="llama3-8b-8192"

    groq_chat = ChatGroq(
            groq_api_key=api_key, 
            model_name=model
    )

    chain = groq_sys_prompt | groq_chat | StrOutputParser()
    response = chain.invoke({"user_prompt": prompt})
    #response = "I am your assistant"
    st.chat_message('assistant').markdown(response)
    st.session_state.messages.append(
            {'role':'assistant', 'content':response})
    
