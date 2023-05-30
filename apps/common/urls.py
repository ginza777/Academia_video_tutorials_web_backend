from django.urls import path
from .views import *

urlpatterns = [

    #courses

    path('courses/', CoursesListAPIView.as_view()),
    path('courses/<int:pk>/', CoursesDetailAPIView.as_view()),
    path('courses/create/', CoursesCreateAPIView.as_view()),
    path('courses/update/<int:pk>/', CoursesUpdateAPIView.as_view()),
    path('courses/delete/<int:pk>/', CoursesDeleteAPIView.as_view()),

    #teachers

    path('teachers/', TeachersListAPIView.as_view()),
    path('teachers/<int:pk>/', TeachersDetailAPIView.as_view()),
    path('teachers/create/', TeachersCreateAPIView.as_view()),
    path('teachers/update/<int:pk>/', TeachersUpdateAPIView.as_view()),
    path('teachers/delete/<int:pk>/', TeachersDeleteAPIView.as_view()),

    #contact_us

    path('contact_us/', ContactCreateAPIView.as_view()),

    #blogposts

    path('blogposts/', BlogpostsListAPIView.as_view()),
    path('blogposts/<int:pk>/', BlogpostsDetailAPIView.as_view()),
    path('blogposts/<int:pk>/comments', BlogpostsDetailCommentsAPIView.as_view()),
    path('blogposts/create/', BlogpostsCreateAPIView.as_view()),
    path('blogposts/update/<int:pk>/', BlogpostsUpdateAPIView.as_view()),
    path('blogposts/delete/<int:pk>/', BlogpostsDeleteAPIView.as_view()),

    #post_comments

    path('post_comments/', PostCommentsListAPIView.as_view()),
    path('post_comments/<int:pk>/', PostCommentsDetailAPIView.as_view()),
    path('post_comments/create/', PostCommentsCreateAPIView.as_view()),
    path('post_comments/update/<int:pk>/', PostCommentsUpdateAPIView.as_view()),
    path('post_comments/delete/<int:pk>/', PostCommentsDeleteAPIView.as_view()),

    #news

    path('news/', NewsListAPIView.as_view()),
    path('news/create/', NewsCreateAPIView.as_view()),



    ]
