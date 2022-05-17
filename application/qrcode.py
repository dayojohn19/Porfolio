import os
import qrcode
from django.shortcuts import render


def main(request):
    # try:
    if request.POST != 'POST':
        # pass
        return render(request, 'application/qrcode.html', {
            'message': 'yeas?'
        })
    else:
        qr = request.POST["qrcode"]
        img = qrcode.make(qr)
        img.save("qr.png", "PNG")
        os.system("open qq.png")
        return render(request, 'application/qrcode.html', {
            'message': img
        })
        # WIth background
        # print('yes post')
        # from PIL import Image
        # img_bg = Image.open('qrback.png')
        # # qr = qrcode.QRCode(box_size=4)
        # # qr.add_data('Garage Sale')
        # # qr.make()
        # # img_qr = qr.make_image()
        # #
        # qr = request.POST["qrcode"]
        # img = qrcode.make(qr)
        # img.save("qr.png", "PNG")
        # qr = qrcode.QRCode(box_size=1)
        # qr.add_data('Garage')
        # img_qr = qrcode.make(qr)
        # #
        # # img_qr = qr.make_image()
        # position = (img_bg.size[0] - img_qr.size[0],
        #             img_bg.size[1]-img_qr.size[1])
        # img_bg.paste(img_qr, position)
        # img_bg.save('qrfinal.png')
        # os.system("open qrfinal.png")

    # except:
    return render(request, 'application/qrcode.html', {
        'message': 'no thanks'
    })
   # qr = request.POST["qrcode"]
    # img = qrcode.make(qr)
    # img.save("qr.png", "PNG")
    # os.system("open qq.png")
    # return render(request, 'application/qrcode.html', {
    #     'message': img
    # })
    # WIth background


# def main(request):
#     img = qrcode.make("https://www.google.com/?client=safari")
#     # img.save("qr.png", "PNG")
#     os.system("open qr.png")
#     return render(request, 'application/earthquake.html')


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
