from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.models import Avg
from django.core.paginator import Paginator

from .forms import (UserForm,
                    ProfileEditForm)
from .models import (Profile,
                     Category,
                     Product,
                     Comments)


def IndexView(request):
    ''' Представление для отображения главной страницы'''
    
    category = Category.objects.all()
    
    return render(request, 'main/index.html', {'category': category})


def AboutView(request):
    ''' Представление для отображения страницы "О нас" '''
    category = Category.objects.all()
    
    return render(request, 'main/about.html', {'category': category})


def ShopView(request):
    ''' Представление для отображения страницы "Магазин" '''
    # Берем обьекты для отображения на странцие
    product = Product.objects.all()
    category = Category.objects.all()
    comments = Comments.objects.all()
    
    # Пагинация продуктов
    paginator = Paginator(product, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Сортировка продуктов 
    if request.method == 'GET':
        sort_by_name = request.GET.get('sort_by_name')
        sort_by_price = request.GET.get('sort_by_price')
        sort_by_brand = request.GET.get('sort_by_brand')
        
        if sort_by_name:
            product = Product.objects.order_by('name')
            
        if sort_by_brand:
            product = Product.objects.order_by('brand')
            
        if sort_by_price:
            product = Product.objects.order_by('price')
    
    # Создаем словарь для передачи данных на страницу
    context = {
        'product': product,
        'category': category,
        'comments': comments,
        'page_obj': page_obj
    }
    
    return render(request, 'main/shop.html', context=context)


def ProductDetailView(request, slug):
    ''' Представлние для отображения страницы одного продукта'''
    
    # Передаем обьект который равен слагу продукта 
    # из базы для отоюражения деталей продукта
    product = get_object_or_404(Product, slug=slug)
    
    context = {
        'product': product
    }
    return render(request, 'main/product-detail.html', context=context)


def ContactsView(request):
    ''' Представление для отображения страницы контактов и для связи'''
    
    category = Category.objects.all()
    
    return render(request, 'main/contacts.html', {'category': category})


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


def ProfileEditView(request):
    
    '''Представления для редактирования пользователя'''
    if request.user.is_authenticated:
        if request.method == 'POST':
            FormProfile = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
            FormUser = UserForm(request.POST, request.FILES, instance=request.user)
            
            if FormProfile.is_valid() and FormUser.is_valid():
                FormProfile.save()
                FormUser.save()
                messages.success(request, 'Редактирование прошло успешно')
                return redirect('/profile')
            
            
    FormProfile = ProfileEditForm(instance=request.user.profile)
    FormUser = UserForm(instance=request.user)
    context = {
        'FormProfile': FormProfile,
        'FormUser': FormUser,
    }
    return render(request, 'profile/edit-profile.html', context=context)

