from django.urls import path
from . import views
 
app_name = "reviewer"
urlpatterns = [
    path("", views.index, name="index"),
    path("questions/<str:department>/<str:level>",
         views.question, name="question"),
    path('questions/<str:department>/<str:level>/<str:user_function>/getit',
         views.new_question, name="new_question"),
    # path('new_question', views.new_question, name="new_question"),
    path('add_score/<str:side>/<str:tries>/<str:score>/<str:user_ip>',
         views.add_score, name="add_score"),
    path('get_score/<str:ip>', views.get_score, name="get_score"),
    path('ip/register/<str:user_ip>',   views.register_ip, name="register_ip")
]
     