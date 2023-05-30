from django.contrib import admin
from .models import Teacher,CustomUser,Contact,News,Blogpost,PostComments,Course,Starts
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
# Register your models here.
@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    pass
# Register your models here.
@admin.register(PostComments)
class PostCommentsAdmin(admin.ModelAdmin):
    pass
# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','price_per')
# Register your models here.
@admin.register(Starts)
class StartsAdmin(admin.ModelAdmin):
    pass
# Register your models here.

