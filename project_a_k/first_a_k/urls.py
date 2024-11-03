from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_a_k, name='first_a_k'),
    path('lesson/<str:pk>/', views.lesson, name='lesson'),
    path('create-lesson/', views.create_lesson, name='create-lesson'),
    path('index/', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('room/', views.room, name='room'),
]
