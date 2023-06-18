import openai
import streamlit as st
from streamlit_chat import message as Mess
import os
import ask_page
GPT_MODEL = "gpt-3.5-turbo"
# openai_api_key=os.getenv('OPENAI_API_KEY')

# st.title("💬 烟台南山学院 GPT")
# # openai.api_key = st.secrets.openai_api_key
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "你好同学有什么可以帮助你的"}]
# with st.form("chat_input", clear_on_submit=True):
#     a, b = st.columns([4, 1])
#     user_input = a.text_input(
#         label="Your message:",
#         placeholder="What would you like to say?",
#         label_visibility="collapsed",
#     )
#     b.form_submit_button("Send", use_container_width=True)
#
# for msg in st.session_state.messages:
#     message(msg["content"], is_user=msg["role"] == "user",avatar_style="big-ears")
#
# if user_input:
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     message(user_input, is_user=True)
#     msg = ask_page.ask(query=st.session_state.messages, model=GPT_MODEL,token_budget=2000 - 500)
#     st.session_state.messages.append(msg)
#     message(msg.content)

#
# st.session_state
#
with st.sidebar:
    openai_api_key = st.text_input('OpenAI API Key', key='chatbot_api_key')
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Streamlit GPT")
# openai.api_key = st.secrets.openai_api_key
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([4, 1])
    user_input = a.text_input(
        label="Your message:",
        placeholder="What would you like to say?",
        label_visibility="collapsed",
    )
    b.form_submit_button("Send", use_container_width=True)

for msg in st.session_state.messages:
    Mess(msg["content"], is_user=msg["role"] == "user")

if user_input and not openai_api_key:
    st.info("Please add your OpenAI API key to continue.")

if user_input and openai_api_key:
    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": user_input})
    Mess(user_input, is_user=True)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    Mess(msg.content)