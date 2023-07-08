from django.contrib import admin
from .models import (Profile,
                     Category, 
                     Comments, 
                     Product,
                     SizeChoices,
                     ColorChoices,)


admin.site.register(ColorChoices)
admin.site.register(SizeChoices)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comments)
