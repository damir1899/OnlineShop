from django.urls import path
from .views import (IndexView,
                    AboutView,
                    ShopView,
                    ContactsView,
                    ProfileUserView, 
                    LoginUserView, 
                    RegistrationUserView,
                    ProductDetailView,
                    LogoutUserView)

urlpatterns = [
    path('', IndexView),
    path('about/', AboutView),
    path('shop/', ShopView),
    path('contacts/', ContactsView),
    path('profile/', ProfileUserView),
    path('login/', LoginUserView),
    path('registration/', RegistrationUserView),
    path('logout/', LogoutUserView),
    path('shop/<slug:slug>/', ProductDetailView, name='product_detail'),

]