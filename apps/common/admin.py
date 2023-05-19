from django.contrib import admin
from .models import Teacher
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
# Register your models here.
