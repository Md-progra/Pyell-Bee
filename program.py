import pyttsx3
import SpeechRecognition as sr
import time 
import tkinter as tk
from tkinter import messagebox
  # Creating the function to listen, recognize and convert
   def listen_convert_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening to you...")
        audio = recognizer.listen(source)
        print("Recognizing...")
        try:
            text= recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand what you said")
                return "Sorry, I couldn't understand what you said"
                messagebox.showerror("Error", "Sorry I couldn't understand what you said")
