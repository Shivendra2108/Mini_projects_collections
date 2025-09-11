import pyttsx3 

engine = pyttsx3.init()
i = input ("Write anything: ")
engine.say(i)
engine.runAndWait()