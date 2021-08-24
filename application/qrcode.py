import os
import qrcode
from django.shortcuts import render

def main(request):
    img = qrcode.make("https://www.google.com/?client=safari")
    # img.save("qr.png", "PNG")
    os.system("open qr.png")
    return render(request, 'application/earthquake.html')



# from django.shortcuts import render
# import pyttsx3

# def main(request):
#     engine = pyttsx3.init()
#     name = "John Chrostoper"
#     engine.say(f"hello, {name} where are you going to")
#     try:
#         engine.runAndWait(),
#     except:
#         pass
#     return render(request, 'application/earthquake.html',{
        
#     })




# img.save("qr.png", "PNG")
# os.system("open qr.png")

