from django.contrib import admin
from .models import (Profile,
                     Category, 
                     Comments, 
                     Product)


admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Product)
