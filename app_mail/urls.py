from django.urls import path

from . import views
app_name="mail"
urlpatterns = [
    path("", views.index, name="index"),
    path("application/login", views.login_view, name="login"),
    path("application/logout", views.logout_view, name="logout"),
    path("application/register", views.register, name="register"),

    # API Routes
    path("application/emails", views.compose, name="compose"),
    path("application/contact", views.contact, name="contact"),
    path("application/emails/<int:email_id>", views.email, name="email"),
    path("application/emails/<str:mailbox>", views.mailbox, name="mailbox"),
]
