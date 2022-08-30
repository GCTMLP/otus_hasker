from django.urls import include, re_path, path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

# Набор URL, отвечающих за вход, выход и регистрицию в app accounts
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path("register/", views.register_request, name="register"),
]