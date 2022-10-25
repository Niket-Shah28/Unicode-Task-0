from django.contrib import admin
from .models import todo

# Register your models here.
@admin.register(todo)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','Title','Note','Count','Save_Date','name','Last_Date','Status')