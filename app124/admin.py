from django.contrib import admin
from .models import UserModel
# Register your models here.
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','contact_no','gender','pin','city','state',
                    'gmail','password','profile_image']
