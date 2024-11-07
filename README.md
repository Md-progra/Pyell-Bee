# Pyell-Bee
 Basically got this idea when I was working with a for loop and a string *lol*. This program is expected to listen to a word, switch it to text, spell out the letters of the word one after the other to the user 
 Speech-to-Text: Use speech_recognition to capture spoken words and convert them into text.
Iterate and Spell: Split the recognized text into individual words, then split each word into letters.
Text-to-Speech (TTS): Use pyttsx3 to spell each word letter by letter in audio.


How does it work!
listen_and_convert_to_text(): This function listens to audio from the microphone, converts it to text using Google's Web Speech API, and returns the recognized text.
spell_back_in_audio(): This function spells each word letter by letter using the pyttsx3 TTS engine. A slight delay between letters makes the spelling clearer.
