from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hasker.settings.models import Profile


class NewUserForm(UserCreationForm):
	"""
	Класс отрисовки формы регистрации
	"""
	email = forms.EmailField(required=True)
	foto = forms.ImageField()
	# Указываем модель и поля модели для отрисовки формы
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2", "foto")

	# Метод сохранения данных в бд
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class LoginForm(forms.Form):
    """
    Класс отрисовки формы входа
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)