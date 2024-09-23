from django.shortcuts import render, redirect
from .models import Administrator
from .forms import AdministratorForm


# страница, где все уроки
def first_a_k(request):
    adm = Administrator.objects.all()
    context = {
        'first_a_k': adm,
    }
    return render(request, 'first_a_k/projects.html', context)


# страница с описанием урока
def lesson(request, pk):
    lesson_obj = Administrator.objects.get(id=pk)
    return render(request, 'first_a_k/single-lesson.html', {'lesson': lesson_obj})


# админ может заполнять некоторые данные не заходя в админку
def create_lesson(request):
    form = AdministratorForm()
    context = {
        'form': form,
    }
    return render(request, 'first_a_k/forma.html', context)
