from django.contrib import admin

from .models import Car
admin.site.register(Car)

from .models import Questions
admin.site.register(Questions)

# Register your models here.
