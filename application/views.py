from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def sendit(request, contact,    user_name,  message):
    if request.method == 'POST':
        print('\n')
        print('\nContact: ', contact)
        print('\nName: ', user_name)
        print('\nMessage: ', message)
        print('\n')
        import smtplib
    # fun-fact: from is a keyword in python, you can't use it as variable, did abyone check if this code even works?
        fromMy = 'JohnFNG@yahoo.com'
        to = 'repapaka20@gmail.com', 'dayo_john16@yahoo.com'
        subj = f'{contact} is Contacting YOU John Foreign'
        date = '2/1/2010'
        msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (
            fromMy, to, subj, date, message)
        username = str('johnwebsiteprojects@gmail.com')
        password = str('aaa09094553940')

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.ehlo()
        server.login(username, password)

        contact_to = contact
        contact_subj = message
        contact_date = '2/1/2012'
        contact_message = "Thank You for reaching Us.. "

        contact_msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (
            fromMy, contact_to, contact_subj, contact_date, contact_message)

        server.sendmail(fromMy, contact, contact_msg)
        server.sendmail(fromMy, to, msg)
        server.quit()
        print('ok the email has sent ')
        # except :
        print('can\'t send the Email')


def app_mail(request):
    if request.user.is_authenticated:
        return render(request, 'mail/inbox.html')
    return render(request, "user/login.html")

    # return redirect('user:index')

    # return render(request, 'mail/login.html')


def application(request):
    return render(request, 'application/application.html')


def news(request):
    return render(request, 'news/index.html')


def course_booking(request):
    return redirect('news:index')

    # return render(request, 'course_booking/index.html')
