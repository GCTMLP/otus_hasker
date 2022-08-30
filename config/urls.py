from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('settings/', include('hasker.settings.urls')),
    path('auth/', include('hasker.accounts.urls')),
    path('', include('hasker.questions.urls')),
    path('answers/', include('hasker.answers.urls')),
]

