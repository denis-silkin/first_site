from django.shortcuts import render, redirect
from .models import Administrator
from .forms import AdministratorForm
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# вход на сайт
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'Имя пользователя не существует!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Имя пользователя или пароль не корректные!')

    return render(request, 'first_a_k/login.html')


# выход с сайта
def logout_user(request):
    logout(request)
    messages.info(request, 'Пользователь вышел из аккаунта')
    return redirect('login')


# страница, где все темы + поиск + пагинация
def first_a_k(request):
    # поиск
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    adm = Administrator.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    # пагинация
    page = request.GET.get('page')
    results = 4
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
def index(request):
    return render(request, 'first_a_k/index.html')

