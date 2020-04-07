import speech_recognition as sr
from time import sleep
t=''
def tts(recg,aud):
    try:
        global t
        t=rcg.recognize_google(aud)
    except Exception as e:
        print(e)
r=sr.Recognizer()
r.listen_in_background(sr.Microphone(),tts)
while True:
    if t:
        print(t)
        t=''
    print('Say:')
    sleep(0.1)
