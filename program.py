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
    # Creating a function to spell back to user
    def spell_back_in_audio(text):

        engine = pyttsx3.init() #initializing the engine
        engine.setProperty('rate', 150) #setting the rate of speech
        words = text.split() #splitting the text into letters

        for word in words: #looping through the words to spell them back
            for letter in word: # looping through the letters 
            engine.say(letter): 
            engine.runAndWait() #running the engine
            time.sleep(1)  #pauses for a second

            # engine.say(" ") #pauses for a second
            # engine.runAndWait()
    # Creating the listeening function
    def start_to_listen():
        tex = listen_convert_to_text()
        if text:
            spell_back_in_audio(text)
  
  # Creation of GUI
  root = tk.Tk() #Creating thr root window
  root.title("Pyell Bee") #Setting title of program

  frame = tk.Frame(root,bg = "lightblue",padx = 10,pady=10,bd = 5, relief = tk.RAISED) #Creating and setting/designing the frame


