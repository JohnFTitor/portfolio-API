from knox.views import LogoutView
from django.urls import path
from .views import LoginView

urlpatterns = [
    path('login', LoginView.as_view(), name='user_login'),
    path('logout', LogoutView.as_view(), name='user_logout'),
]
