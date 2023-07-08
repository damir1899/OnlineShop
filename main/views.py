from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.models import Avg

from .forms import UserForm
from .models import (Profile,
                     Category,
                     Product,
                     Comments)


def IndexView(request):
    return render(request, 'main/index.html')


def AboutView(request):
    return render(request, 'main/about.html')


def ShopView(request):
    product = Product.objects.all()
    category = Category.objects.all()
    comments = Comments.objects.all()
    # average = Comments.objects.aggregate(avg=Avg('rating'))
    
    context = {
        'product': product,
        'category': category,
        'comments': comments
    }
    return render(request, 'main/shop.html', context=context)

def ProductDetailView(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    context = {
        'product': product
    }
    return render(request, 'main/product-detail.html', context=context)


def ContactsView(request):
    return render(request, 'main/contacts.html')


def ProfileUserView(request):
    ''' Представление для отображения информациий на странице профиля'''
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        context = {
            'profile': profile
        }
        return render(request, 'profile/profile.html', context=context)
    else:
        return redirect('/login')


def LoginUserView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            try:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Вы успешно вошли!')
                    return redirect("/")
                else:
                    messages.error(request, 'Неверное имя пользователя или пароль.')
            except Exception as e:
                messages.error(request, 'Произошла ошибка при аутентификации. Пожалуйста, попробуйте снова.')
        else:
            messages.error(request, 'Пожалуйста, введите имя пользователя и пароль.')
            
    return render(request, 'profile/login.html')


# Выход с аккаунта
def LogoutUserView(request):
    logout(request)
    return redirect('/')


# Функция для регистраций пользователя
def RegistrationUserView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.password != request.POST.get('password2'):
                messages.error(request, 'Пароли не совпадают')
                return redirect('/registration')
            else:
                user.set_password(user.password)
                form.save()
                messages.success(request, 'Регистрация прошла успешно')
                return redirect('/')
    else:
        form = UserForm()
        
    return render(request, 'profile/registration.html', {'form': form})

