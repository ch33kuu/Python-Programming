import pyttsx3
eng=pyttsx3.init()
eng.setProperty('rate',100)
eng.setProperty('volume',1.0)
eng.say('')
eng.runAndWait()
