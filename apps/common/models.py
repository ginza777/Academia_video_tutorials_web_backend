from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Choice(models.TextChoices):
    customer = 'customer',
    admin = 'admin',
    manager = 'manager',
    employee = 'employee'
    teacher = 'teacher'
    block = 'block'
    test = 'student'


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    phone = PhoneNumberField(blank=True, null=True)
    privaligies = models.CharField(max_length=150, choices=Choice.choices, default=Choice.customer)
    token_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    avatar = models.ImageField(upload_to='images/user/avatar/', blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'CustomUser'
        db_table = 'GinzaAuthUser_customuser'

    def __str__(self):
        return self.username


# Create your models here.
class Teacher(models.Model):
    fistname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = PhoneNumberField(blank=True, null=True)
    image = models.ImageField(upload_to='images/teacher/', blank=True)
    description = models.TextField(blank=True)
    position = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    facebook = models.CharField(max_length=20, blank=True)
    twitter = models.CharField(max_length=20, blank=True)
    instagram = models.CharField(max_length=20, blank=True)
    telegram = models.CharField(max_length=20, blank=True)
    linkedin = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.fistname

    class Meta:
        verbose_name_plural = 'Teachers'
        verbose_name = 'Teacher'
        db_table = 'teachers'


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contacts'
        verbose_name = 'Contact'
        db_table = 'contacts'


class News(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'News_notification'
        verbose_name = 'News_notification'
        db_table = 'news'


class Blogpost(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='images/blogpost/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Blogposts'
        verbose_name = 'Blogpost'
        db_table = 'blogposts'


class PostComments(models.Model):
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'PostComments'
        verbose_name = 'PostComment'
        db_table = 'postcomments'


class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='images/course/', blank=True)
    description = models.TextField()
    price = models.IntegerField()
    price_per = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Courses'
        verbose_name = 'Course'
        db_table = 'courses'


class Starts(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    count = models.IntegerField()
    token_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f'{self.course.title}'

    class Meta:
        verbose_name_plural = 'Starts'
        verbose_name = 'Start'
        db_table = 'starts'


#test


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Videos'
        verbose_name = 'Video'
        db_table = 'Videos'



