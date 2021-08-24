
# import speech_recognition
# import pyttsx3
# def main(request):
#     engine = pyttsx3.init()
#     name = "John Chrostoper"
#     engine.say(f"hello, {name} where are you going to")
#     try:
#         engine.runAndWait()

#     except:
#         pass

    
#     recognizer = speech_recognition.Recognizer()
    
#     with speech_recognition.Microphone() as source:


#         print("Say Something: ")
#         audio = recognizer.listen(source)
#         words = recognizer.recognize_google(audio)

#     print("You said: ")
#     print(str(words))

#     # words = input("saying something: ").lower()
#     #engine to speak




#     if "hello" and "me" in words:
#         # print("Hello to you too!")
#         engine.say(f"hello, {words} where are you going to")
#         engine.runAndWait()
#         engine.stop()
#         print("engine stopped")
#         print("Say Something voice2: ")
#         with speech_recognition.Microphone() as source:
#             voice2 = recognizer.listen(source)
#             words = recognizer.recognize_google(voice2)
#             engine.say(words)
#             engine.runAndWait()
#             engine.stop()
#             print("engine stopped")

#     elif "how are you" in words:
#         print("I am well, thanks")
#     elif "goodbye" in words:
#         print("Goodbye to you too!")
#     else:
#         print("huh?")