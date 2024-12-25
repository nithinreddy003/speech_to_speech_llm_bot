# Speech-to-Speech Bot

A **Speech-to-Speech Bot** built using Python, Streamlit, SpeechRecognition, pyttsx3, and the Gemini API. This bot listens to your voice, transcribes it into text, processes it through the Gemini API for a response, and then speaks the response back to you. 

---

## Features

1. **Speech Recognition**: Converts spoken input into text using Google's SpeechRecognition library.
2. **Gemini API Integration**: Processes the transcribed text with Gemini API for intelligent and contextual responses.
3. **Text-to-Speech**: Converts the Gemini API's response into speech using pyttsx3.
4. **Streamlit Interface**: Provides an interactive web-based interface for the user.

---

## How It Works

1. Click the **Start** button to begin speech recognition.
2. Speak into your microphone, and the bot will transcribe your speech into text.
3. The transcribed text is sent to the Gemini API for processing.
4. The Gemini API generates a response, which is displayed on the Streamlit interface.
5. The bot speaks the response back to you.

---

## Requirements

Ensure you have the following dependencies installed:

- **Python 3.8+**
- `streamlit`
- `speechrecognition`
- `pyttsx3`
- `requests`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nithinreddy003/speech_to_speech_llm_bot.git
   cd speech_to_speech_llm_bot
