from django.shortcuts import render, redirect
from .models import Administrator
from .forms import AdministratorForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError


# вход на сайт
def login_user(request):
    if request.method == 'GET':
        return render(request, 'first_a_k/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'first_a_k/login.html', {'form': AuthenticationForm(),
                          "error": 'Имя пользователя или пароль не корректные!'})
        else:
            login(request, user)
            return redirect('index')


# выход с сайта
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'Пользователь вышел из аккаунта')
        return redirect('login')


# страница, где все темы + поиск + пагинация
@login_required(login_url='login')
def first_a_k(request):
    # поиск
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    adm = Administrator.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    # пагинация
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(adm, results)

    try:
        adm = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        adm = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        adm = paginator.page(page)

    context = {
        'first_a_k': adm,
        'search_query': search_query,
        'paginator': paginator,
    }
    return render(request, 'first_a_k/projects.html', context)


# страница с описанием урока
def lesson(request, pk):
    lesson_obj = Administrator.objects.get(id=pk)
    return render(request, 'first_a_k/single-lesson.html', {'lesson': lesson_obj})


# админ может заполнять данные не заходя в админку
@login_required(login_url='login')
def create_lesson(request):
    form = AdministratorForm()

    if request.method == 'POST':
        form = AdministratorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('first_a_k')
    context = {
        'form': form,
    }
    return render(request, 'first_a_k/forma.html', context)


# главная страница
@login_required(login_url='login')
def index(request):
    return render(request, 'first_a_k/index.html')


# регистрация
def register(request):
    if request.method == 'GET':
        return render(request, 'first_a_k/register.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'first_a_k/register.html', {'form': UserCreationForm(), 'error': 'Имя '
                                                                                                        'пользователя '
                                                                                                        'существует'})
        else:
            return render(request, 'first_a_k/register.html', {'form': UserCreationForm(), 'error': 'Пароли не '
                                                                                                    'совпадают'})
