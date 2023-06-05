from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import \
    CoursesListAPIView, CoursesDetailAPIView, CoursesCreateAPIView, CoursesUpdateAPIView, \
    CoursesDeleteAPIView, CoursesDetailVideoAPIView, TeachersListAPIView, TeachersDetailAPIView, TeachersCreateAPIView, \
    TeachersUpdateAPIView, TeachersDeleteAPIView, ContactCreateAPIView, BlogpostsListAPIView, BlogpostsDetailAPIView, \
    BlogpostsCreateAPIView, BlogpostsUpdateAPIView, BlogpostsDeleteAPIView, BlogpostsDetailCommentsAPIView, \
    PostCommentsListAPIView, PostCommentsDetailAPIView, PostCommentsCreateAPIView, PostCommentsUpdateAPIView, \
    PostCommentsDeleteAPIView, NewsListAPIView, NewsCreateAPIView, CustomAuthToken,\
    MyTokenObtainPairView, CustomUserRegister, DeleteUser

urlpatterns = [
    # auth
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('token/', MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('register/', CustomUserRegister.as_view(), name='registration'),
    path('delete/', DeleteUser.as_view(), name='delete'),
    # courses
    path('courses/', CoursesListAPIView.as_view()),
    path('courses/<int:pk>/', CoursesDetailAPIView.as_view()),
    path('courses/create/', CoursesCreateAPIView.as_view()),
    path('courses/update/<int:pk>/', CoursesUpdateAPIView.as_view()),
    path('courses/delete/<int:pk>/', CoursesDeleteAPIView.as_view()),
    # videos
    path('courses/<int:pk>/videos/', CoursesDetailVideoAPIView.as_view()),
    # teachers
    path('teachers/', TeachersListAPIView.as_view()),
    path('teachers/<int:pk>/', TeachersDetailAPIView.as_view()),
    path('teachers/create/', TeachersCreateAPIView.as_view()),
    path('teachers/update/<int:pk>/', TeachersUpdateAPIView.as_view()),
    path('teachers/delete/<int:pk>/', TeachersDeleteAPIView.as_view()),
    # contact_us
    path('contact_us/', ContactCreateAPIView.as_view()),
    # blogposts
    path('blogposts/', BlogpostsListAPIView.as_view()),
    path('blogposts/<int:pk>/', BlogpostsDetailAPIView.as_view()),
    path('blogposts/<int:pk>/comments', BlogpostsDetailCommentsAPIView.as_view()),
    path('blogposts/create/', BlogpostsCreateAPIView.as_view()),
    path('blogposts/update/<int:pk>/', BlogpostsUpdateAPIView.as_view()),
    path('blogposts/delete/<int:pk>/', BlogpostsDeleteAPIView.as_view()),
    # post_comments
    path('post_comments/', PostCommentsListAPIView.as_view()),
    path('post_comments/<int:pk>/', PostCommentsDetailAPIView.as_view()),
    path('post_comments/create/', PostCommentsCreateAPIView.as_view()),
    path('post_comments/update/<int:pk>/', PostCommentsUpdateAPIView.as_view()),
    path('post_comments/delete/<int:pk>/', PostCommentsDeleteAPIView.as_view()),
    # news
    path('news/', NewsListAPIView.as_view()),
    path('news/create/', NewsCreateAPIView.as_view()),

]
