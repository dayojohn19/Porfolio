from django.shortcuts import render
import pyttsx3

def main(request):
    engine = pyttsx3.init()
    name = "John Chrostoper"
    engine.say(f"hello, {name} where are you going to")
    try:
        engine.runAndWait(),
    except:
        pass
    return render(request, 'application/earthquake.html',{
        
    })