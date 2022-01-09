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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('a_index.urls')),
    path('blog/', include('a_blog.urls')),
    path('street_race/', include('a_street_race.urls')),
    path('games/', include('games.urls')),
    path('app_mail/', include('app_mail.urls')),
    path('application/', include('application.urls')),
    path('a_social_network/', include('a_social_network.urls')),
    path('g_pigeon_race/', include('g_pigeon_race.urls')),
    path('user/', include('user.urls')),
    path('app_food/', include('app_food.urls')),
    path('app_news/', include('app_news.urls')),
    path('app_course_booking/', include('app_course_booking.urls')),
    path('commerce/', include('commerce.urls')),
    path('com_auction/', include('com_auction.urls')),
    path('com_sale/', include('com_sale.urls')),
    path('com_bank/', include('com_bank.urls')),
    path('app_hiring/', include('app_hiring.urls')),
    path('com_trade/', include('com_trade.urls')),
    path('ubx/', include('ubx.urls')),
    # path('app_freedive/', include('app_freedive.urls')),
    path('app_event/', include('app_event.urls')),
    path('app_pipa/', include('app_pipa.urls')),
    path('com_invest/', include('com_invest.urls')),
    path('app_diary/', include('app_diary.urls')),
    path('reviewer/', include('reviewer.urls'))
]

# Pigeon Config

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
##
