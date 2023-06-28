from django.db import models
from django.contrib.auth.models import User
# from .utils import validate_phone_number


COLORS_CHOICES = (
    ('white', 'white'),
    ('black', 'black'), 
    ('yellow', 'yellow'), 
    ('green', 'green'), 
    ('blue', 'blue')
)


class Profile(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE, 
                                verbose_name='Пользователь')
    phone = models.CharField(max_length=20, 
                             verbose_name='Номер телефона', blank=True, null=True)
    adress = models.CharField(max_length=255, verbose_name='Адрес', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистраций')
    

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    
    def __str__(self) -> str:
        return self.name + ' ' + self.created_at
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'
        

class Comments(models.Model):
    rating = models.PositiveSmallIntegerField(verbose_name='Рейтинг')
    comments = models.TextField(max_length=1000, verbose_name='Комментарий')
    
    def __str__(self) -> str:
        return self.rating
        

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    brand = models.CharField(max_length=50, verbose_name='Бренд')
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, verbose_name='Комментарий')
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    
    def __str__(self) -> str:
        return f'{self.name} {self.brand} {self.price}'
    
    
