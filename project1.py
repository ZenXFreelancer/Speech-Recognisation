import speech_recognition as s

#create a object for Recognizer

sr=s.Recognizer()
print("I'm listening zayd boss......")
with s.Microphone() as m:
    audio=sr.listen(m)
    query=sr.recognize_google(audio,language='eng-in')
    print(query)
