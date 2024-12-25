from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/recommendations/', views.career_recommendation, name='recommendations'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login_view'),
]
