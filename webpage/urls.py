"""webpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', include('a_index.urls')),
    path('blog/', include('a_blog.urls')),
    path('street_race/', include('a_street_race.urls')),
    path('games/', include('games.urls')),
    path('app_mail/', include('app_mail.urls')),
    path('application/', include('application.urls')),
    path('a_social_network/', include('a_social_network.urls')),
    path('g_pigeon_race/', include('g_pigeon_race.urls')),
    path('', include('user.urls')),
    path('app_food/', include('app_food.urls')),
    path('app_news/', include('app_news.urls')),
    path('app_course_booking/', include('app_course_booking.urls')),

]

### Pigeon Config
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
##