import time
import streamlit as st
import pandas as pd 
import numpy as np 
import gpt

st.title("HelpMeSpeak")
st.text("Welcome to your language learning journey!")
st.text("We will help you speak any language of your choice within minutes!")

st.divider()
def prompt():
    languages_supported = ["", "Afrikaans", "Arabic", "Armenian", "Azerbaijani", "Belarusian", 
                           "Bosnian", "Bulgarian", "Catalan", "Chinese", "Croatian", "Czech", 
                           "Danish", "Dutch", "English", "Estonian", "Finnish", "French", "Galician", 
                           "German", "Greek", "Hebrew", "Hindi", "Hungarian", "Icelandic", "Indonesian", 
                           "Italian", "Japanese", "Kannada", "Kazakh", "Korean", "Latvian", "Lithuanian", 
                           "Macedonian", "Malay", "Marathi", "Maori", "Nepali", "Norwegian", "Persian", 
                           "Polish", "Portuguese", "Romanian", "Russian", "Serbian", "Slovak", "Slovenian", 
                           "Spanish", "Swahili", "Swedish", "Tagalog", "Tamil", "Thai", "Turkish", "Ukrainian", 
                           "Urdu", "Vietnamese", "Welsh"]
    language_selection = st.selectbox("Pick a language: ", languages_supported)
    st.divider()
    st.markdown("Ex: I want to speak in a... **business meeting**.")
    story_input = st.text_input("I want to speak ...", max_chars=25)
    story_input = str.lower(story_input)
    user_api_key = st.text_input("Enter your OpenAI API-KEY: ")
    clicked = st.button("Learn!", type="primary", disabled=(True if (story_input == "" or language_selection == "") else False))
    if clicked:
        generate_text(language_selection, story_input, user_api_key)
            

def display_text(txt):
    for t in txt:
        yield t
        time.sleep(0.01)

def generate_text(language, prompt, user_api_key):
    st.divider()
    st.subheader("Let's Learn " + language + "!")
    with st.spinner('Wait for it...'):
        response = gpt.fetch_response(language, prompt, user_api_key)
    st.write_stream(display_text(response))
    return True
        

prompt()


