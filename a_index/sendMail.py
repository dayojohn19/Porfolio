from django.shortcuts import render
print('SEnding Mail.....')
mail = 0


def sendmail(request):
    global mail
    mail +=1
    print('Yeah', mail)
    return render(request, 'a_index/mail.html')