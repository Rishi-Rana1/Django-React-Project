from django.contrib import admin
from .models import Macronutrients, User, TestModel

admin.site.register(Macronutrients)
admin.site.register(User)
admin.site.register(TestModel)