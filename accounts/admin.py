from django.contrib import admin
from .models import CustomUser
from .forms import*
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomCreationForm
    form = CustomChangeForm


admin.site.register(CustomUser, CustomUserAdmin)


