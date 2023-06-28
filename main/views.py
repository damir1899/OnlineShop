from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from main.forms import UserForm


def IndexView(request):
    return render(request, 'main/index.html')


def AboutView(request):
    return render(request, 'main/about.html')


def ShopView(request):
    return render(request, 'main/shop.html')

def ProductDetailView(request):
    return render(request, 'main/product-detail.html')


def ContactsView(request):
    return render(request, 'main/contacts.html')


def ProfileUserView(request):
    return render(request, 'profile/profile.html')


def LoginUserView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        print(username)
        password = request.POST.get("password")
        print(password)
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

