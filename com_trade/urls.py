from django.urls import path
from . import views

app_name = "trade"
urlpatterns = [
    path('', views.index, name="index"),
    path('fetch_data', views.fetch_datas, name="fetch_data"),
    path('live', views.live_chart, name="live"),
    path('new_data', views.new_data, name="new_data"),
    path('primary', views.primary_chart, name="primary_chart")
]
