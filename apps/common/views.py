from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Create your views here.
# auth serializers
from rest_framework import serializers
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .models import CustomUser


class CustomUserSerializerLogin(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "email" and "password".')

        data['user'] = user
        return data


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=9, write_only=True)
    phone = serializers.CharField(max_length=20, min_length=13, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password']

    def create(self, validated_data):
        # Retrieve the password from validated_data
        password = validated_data.pop('password')

        # Hash and encrypt the password using Django's make_password function
        hashed_password = make_password(password)

        # Create the user using the remaining validated_data and the hashed password
        user = CustomUser.objects.create(password=hashed_password, **validated_data)
        return user


class CustomUserSerializerDelete(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


# auth views

class CustomUserRegister(CreateAPIView):
    serializer_class = CustomUserSerializer
    # serializer_class = serializers.UserSerializer
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        print(self.request)
        return self.create(request, *args, **kwargs)


class DeleteUser(APIView):
    serializer_class = CustomUserSerializerDelete
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request)
        print(self.request.user)
        user = CustomUser.objects.get(username=self.request.user)
        date_now = f"{timezone.now().strftime('%Y-%m-%d %H:%M')}"
        user.username = f"{date_now}_deleted_{user.username}"
        user.email = f"{date_now}_deleted_{user.email}"
        user.phone = f"{date_now}_deleted_{user.phone}"
        user.is_active = False
        user.is_staff = False
        user.is_superuser = False
        user.save()
        comment = "User deleted"
        return Response(status=status.HTTP_200_OK, data={"comment": comment})


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomAuthToken(TokenObtainPairView):
    queryset = CustomUser.objects.all()
    serializers_class = CustomUserSerializerLogin


# kurslar
class CourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    teacher_fistname = serializers.CharField(source='teacher.fistname')
    teacher_lastname = serializers.CharField(source='teacher.lastname')
    teacher_image = serializers.ImageField(source='teacher.image')
    videos_count = serializers.SerializerMethodField()

    def get_videos_count(self, course):
        return course.video_set.count()

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'icon',
            'description',
            'price',
            'price_per',
            'created_at',
            'updated_at',
            'token_uuid',
            'teacher',
            'teacher_fistname',
            'teacher_lastname',
            'teacher_image',
            'videos_count',

        )


class CoursesListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.all()


class CoursesDetailAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @swagger_auto_schema(operation_description="Get course by id")
    def get_queryset(self):
        return Course.objects.all()


class CoursesCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.all()


class CoursesUpdateAPIView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.all()


class CoursesDeleteAPIView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.all()


# teachers
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeachersListAPIView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.all()


class TeachersDetailAPIView(RetrieveAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    @swagger_auto_schema(operation_description="Get teacher by id")
    def get_queryset(self):
        return Teacher.objects.all()


class TeachersCreateAPIView(CreateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    def get_queryset(self):
        return Teacher.objects.all()


class TeachersUpdateAPIView(UpdateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    def get_queryset(self):
        return Teacher.objects.all()


class TeachersDeleteAPIView(DestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    def get_queryset(self):
        return Teacher.objects.all()


# contact_us

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def get_queryset(self):
        return Contact.objects.all()


# blogposts

class BlogpostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username')
    created_at = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)
    comments_count = serializers.SerializerMethodField()

    def get_comments_count(self, blogpost):
        return blogpost.postcomments_set.count()

    class Meta:
        model = Blogpost
        fields = ('id', 'title', 'image', 'description', 'created_at', 'username', 'comments_count')


class BlogpostsListAPIView(ListAPIView):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.all()

    def get_queryset(self):
        return Blogpost.objects.all()


class BlogpostsDetailAPIView(RetrieveAPIView):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.all()

    @swagger_auto_schema(operation_description="Get blogpost by id")
    def get_queryset(self):
        return Blogpost.objects.all()


class BlogpostsCreateAPIView(CreateAPIView):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.all()

    def get_queryset(self):
        return Blogpost.objects.all()


class BlogpostsUpdateAPIView(UpdateAPIView):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.all()

    def get_queryset(self):
        return Blogpost.objects.all()


class BlogpostsDeleteAPIView(DestroyAPIView):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.all()

    def get_queryset(self):
        return Blogpost.objects.all()


# post_comments

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    comments = PostCommentSerializer(many=True, read_only=True)
    username = serializers.CharField(source='user.username')
    fist_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    image = serializers.ImageField(source='user.avatar')

    class Meta:
        model = PostComments
        fields = (
            'id',
            'post',
            'user',
            'username',
            'fist_name',
            'last_name',
            'image',
            'comment',
            'created_at',
            'updated_at',
            'comments',
            'updated_at',
        )


class BlogpostsDetailCommentsAPIView(ListAPIView):
    serializer_class = BlogPostSerializer
    queryset = PostComments.objects.all()

    @swagger_auto_schema(operation_description="Get comments by post id")
    def get_queryset(self):
        post_id = self.kwargs['id']
        return PostComments.objects.filter(post_id=post_id)


class PostCommentsListAPIView(ListAPIView):
    serializer_class = PostCommentSerializer
    queryset = PostComments.objects.all()

    def get_queryset(self):
        return PostComments.objects.all()


class PostCommentsDetailAPIView(RetrieveAPIView):
    serializer_class = PostCommentSerializer
    queryset = PostComments.objects.all()

    @swagger_auto_schema(operation_description="Get comment by id")
    def get_queryset(self):
        return PostComments.objects.all()


class PostCommentsCreateAPIView(CreateAPIView):
    serializer_class = PostCommentSerializer
    queryset = PostComments.objects.all()

    def get_queryset(self):
        return PostComments.objects.all()


class PostCommentsUpdateAPIView(UpdateAPIView):
    serializer_class = PostCommentSerializer
    queryset = PostComments.objects.all()

    def get_queryset(self):
        return PostComments.objects.all()


class PostCommentsDeleteAPIView(DestroyAPIView):
    serializer_class = PostCommentSerializer
    queryset = PostComments.objects.all()

    def get_queryset(self):
        return PostComments.objects.all()


# news

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsListAPIView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def get_queryset(self):
        return News.objects.all()


class NewsCreateAPIView(CreateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def get_queryset(self):
        return News.objects.all()


# test

class VideoSerializer(serializers.ModelSerializer):
    file_path = serializers.SerializerMethodField()

    def get_file_path(self, obj):
        return obj.file.url

    class Meta:
        model = Video
        fields = ['title', 'file', 'file_path']


class CoursesDetailVideoAPIView(ListAPIView):
    serializer_class = VideoSerializer

    @swagger_auto_schema(operation_description="Retrieve videos for a specific course")
    def get_queryset(self, *args, **kwargs):
        course_id = self.kwargs['id']
        return Video.objects.filter(course_id=course_id)
