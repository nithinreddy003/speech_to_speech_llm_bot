import streamlit as st
import speech_recognition as sr
import pyttsx3
import requests

engine = pyttsx3.init()
engine.setProperty('rate', 150)  
engine.setProperty('volume', 1)  

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=API_KEY"

st.set_page_config(page_title="Speech-to-Speech Bot", layout="centered")

def recognize_speech():
    """Capture speech from the microphone and convert it to text."""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        st.write("Listening... Please speak into the microphone.")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)

    try:
        st.write("Processing audio...")
        text = recognizer.recognize_google(audio)
        st.write(f"Recognized speech: {text}")
        return text
    except sr.UnknownValueError:
        st.error("Sorry, I didn't catch that.")
        return None
    except sr.RequestError as e:
        st.error(f"Error with the speech service: {e}")
        return None

def get_response_from_gemini(input_text): 
    headers = {"Content-Type": "application/json"}

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": input_text
                    }
                ]
            }
        ]
    }

    try:
        st.write("Sending text to Gemini API...")
        response = requests.post(GEMINI_API_URL, json=data, headers=headers)
        response.raise_for_status()     
        response_data = response.json()
        response_text = response_data['candidates'][0]['content']['parts'][0]['text']
        st.write(f"Gemini Response: {response_text}")
        return response_text
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with Gemini API: {e}")
        return "Sorry, I couldn't process your request."

def speak_text(text): 
    st.write(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

st.title("Speech-to-Speech Bot")
st.write("Click the button below to start speaking.")

if st.button("Start"):
    user_input = recognize_speech()
    if user_input:
        response_text = get_response_from_gemini(user_input)
        speak_text(response_text)
