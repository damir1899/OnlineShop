from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.utils.text import slugify
# from .utils import validate_phone_number


COLORS_CHOICES = (
    ('white', 'white'),
    ('black', 'black'), 
    ('yellow', 'yellow'), 
    ('green', 'green'), 
    ('blue', 'blue')
)

GENDER_CHOICES = (
    ('Мужской', 'Male'),
    ('Женский', 'Female'),
    ('Унисекс', 'Unisex'),
)

def slugify_function(content):
    return slugify(content)

class SizeChoices(models.Model):
    size = models.CharField(max_length=10, verbose_name='Размер')
    
    def __str__(self) -> str:
        return self.size
    
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
        

class Profile(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE, 
                                verbose_name='Пользователь')
    
    image = models.ImageField(upload_to='profile_img/', 
                              verbose_name='Фото профиля', 
                              default='img/shop_01-01.jpg')
    
    phone = models.CharField(max_length=20, 
                             verbose_name='Номер телефона', 
                             default='Укажите номер телефона', 
                             blank=True, 
                             null=True)
    
    address = models.CharField(max_length=255, 
                               verbose_name='Адрес', 
                               default='Укажите адрес')
    
    created_at = models.DateTimeField(auto_now_add=True, 
                                      verbose_name='Дата регистраций')
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'
        


class Product(models.Model):
    image = models.ImageField(upload_to='product_image/', verbose_name='Изображение')
    name = models.CharField(max_length=100, verbose_name='Название')
    brand = models.CharField(max_length=50, verbose_name='Бренд')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    slug = AutoSlugField(populate_from=slugify_function, unique=True, editable=False)
    size = models.ManyToManyField(SizeChoices, verbose_name='Размер')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, verbose_name='Пол')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добвления')
    
    
    def __str__(self) -> str:
        return f'{self.name} {self.brand} {self.price}'
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    
class Comments(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT, verbose_name='Пользователь')
    rating = models.PositiveSmallIntegerField(verbose_name='Рейтинг')
    comments = models.TextField(max_length=1000, verbose_name='Комментарий')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    
    def __str__(self) -> str:
        return f'{self.product} {self.user} {self.rating}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'
    
    
