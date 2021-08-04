from django.contrib import admin

# Register your models here.
from .models import UserData,Feedback

admin.site.register(UserData)
admin.site.register(Feedback)