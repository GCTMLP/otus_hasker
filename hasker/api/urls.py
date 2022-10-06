from django.urls import path, include
from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import views

# Набор URL, отвечающих за перенаправление запросов на необходимые функции
# в app api
urlpatterns = [
    path('questions/search/', views.SearchQuestionApi.as_view()),
    path("questions/", views.QuestionApi.as_view(), name="api_questions",),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    re_path('^questions/(?P<id>.+)/$', views.OneQuestionApi.as_view()),
    re_path('^questions/answers/(?P<id>.+)/$', views.AnswersApi.as_view()),
 ]
