from django.urls import path

from . import views

app_name = "invest"
urlpatterns = [
    path("", views.index, name="index"),
    path("tables", views.table, name="table"),
    path("investors<str:csrf_token>", views.add_investor, name="add_investor"),
    path("reports", views.reports, name="reports"),
    path("about", views.about, name="about"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("reinvest<str:csrf_token>", views.reinvest, name="reinvest")
]
