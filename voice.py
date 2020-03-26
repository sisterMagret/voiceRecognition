import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
	print("say somthing!")
	audio = recognizer.listen(source)
print("Sister Magret speech Recognition thinks you said:\n")
print(recognizer.recognize_google(audio))