import csv
import random
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'reviewer/index.html')


def question(request, department, level):
    return render(request, 'reviewer/question.html')


# DeckManagement = 'ML-D(F1)-Table 1.csv'

DeckManagement = 'decmanagementf1.csv'
firstcsv = 'first.csv'

 
def GetLine(department, level, user_function):
    # with open(f'reviewer/reviewer_question/'+str(DeckManagement), 'r', newline='') as csvfile:
    with open(f'reviewer/reviewer_question/'+str(department)+'/'+str(level)+'/'+str(user_function)+'.csv', 'r', newline='') as csvfile:

        csv_reader = csv.reader(csvfile, delimiter=',')
        firstLines = len((list(csv_reader)))
        return random.randint(1, firstLines-1)


# def new_question(request):

def new_question(request, department, level, user_function):
    print('LOADING')
    print('LOADING', department)
    print('LOADING', level)
    from django.http import JsonResponse
    import csv
    Nline = GetLine(department, level, user_function)
    print(Nline)
    with open(f'reviewer/reviewer_question/'+str(department)+'/'+str(level)+'/'+str(user_function)+'.csv', 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        laman = []
        i = 0
        for row in csv_reader:
            if i < Nline:
                i += 1
                laman.append(row)
            else:
                return JsonResponse(laman[Nline-1], safe=False)


def add_score(request, side, tries, score, user_ip):
    from django.http import JsonResponse
    updateScore(side, score, user_ip, tries)
    return JsonResponse('Success', safe=False)


def get_score(request, ip):
    print("GETTING SCORE")
    from .models import User_score
    from django.http import JsonResponse

    try:

        current_score = User_score.objects.get(ip=ip)
        print(current_score)
        # current_score = current_score.score
        data = [current_score.score,    current_score.tries, ip]
        print('data: ', data)
        return JsonResponse(data, safe=False)

    except:
        print('Oh men')
        return JsonResponse([0, 0], safe=False)


def register_ip(request, user_ip):
    from .models import User_score
    from django.http import JsonResponse

    try:
        current_user = User_score.objects.get(ip=user_ip)
        return JsonResponse('Already Registered', safe=False)

    except:
        current_user = User_score(ip=user_ip)
        current_user.save()
        return JsonResponse('Registered', safe=False)


def updateScore(side, score, ip, tries):
    from .models import User_score
    try:
        current_user = User_score.objects.get(ip=ip)
    except:
        current_user = User_score(ip=ip)
        current_user.save()
    # current_user = User_score.objects.get_or_create(ip=ip)
    # current_user.save()
    print(current_user)
    if side == 'correct':
        current_user.correct += 1
    elif side == 'wrong':
        current_user.wrong += 1
    current_user.tries += 1
    current_user.score = score
    current_user.save()
