from django.urls import path
from . import views
from .views import  register, activate, login_view

app_name = 'authentication'

urlpatterns = [
    path('register', views.register, name="register"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
    path('login/', login_view, name='login'),

]