from django.shortcuts import render

# Create your views here.
from .models import Book, Student
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
####

from app_mail import models as mail
####
class BookCourse(forms.Form):
    price = forms.IntegerField()
    link = forms.CharField()
    instructor = forms.CharField(max_length=64)
    title = forms.CharField(max_length=64)
    description = forms.CharField(widget=forms.Textarea,max_length=100)
    
####

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse("sale:login"))
    if request.method == "GET":
        x = request.user.id
        try:
            Student.objects.get(user=x)
        except:
            s = Student(user=x)
            s.save()
    context = {
        'id':len(Student.objects.all()),
        'courses':Book.objects.all().order_by('id').reverse(),
        'student':Student.objects.all().order_by('id').reverse()
    }
    return render(request, 'course_booking/index.html', context)

##view all students in course
def students(request):
    course = Book.objects.get(id=book_id)
    students = course.enrolless.all()
    return render(request, 'course_booking/index.html', students)

def enroll(request):
    if request.method == "POST":
        course = Book.objects.get(pk=request.POST.get("book_id"))
        student = Student.objects.get(user=request.user.id)
        student.courses.add(course)

        # student_id = request.user.id
        # course = Book.objects.get(pk=book_id)
        # student = Student(user=student_id)

        # try:
        #     Student(user=student_id)
        # except:
        #     student.save()
        # enrollee = Student.objects.get(user=student_id)
        # if enrollee in course.enrollee.all():
        #     x = 'aa'
        # else:
        #     student.courses.add(course)
        #     x = 'bb'
        return render(request, 'course_booking/profile.html',{
        'x': course.enrollee.all()
        })

def create(request):
    context = {
        'create':BookCourse(),
    }
    return render(request, 'course_booking/create.html', context)

def create_course(request):
    if request.method == 'POST':
        form = BookCourse(request.POST)
        if form.is_valid():
            b = Book (
                price = form.cleaned_data["price"],
                instructor = form.cleaned_data["instructor"],
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
                link = form.cleaned_data["link"]
            )
            b.save()
        context = {
            'courses':Book.objects.all().order_by('id').reverse()
        }
        return HttpResponseRedirect(reverse("course_booking:index"))
    else:
        return render(request, 'course_booking/create.html', form)