from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_a_k, name='first_a_k'),
    path('lesson/<str:pk>/', views.lesson, name='lesson'),
    path('create-lesson', views.create_lesson, name='create-lesson'),
]
