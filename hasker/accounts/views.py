from django.shortcuts import  render, redirect
from .forms import NewUserForm, LoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib import messages
from hasker.settings.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings


"""
views в app "accounts" построен на паттерне FBV
"""


def register_request(request):
	"""
	Функция валидации формы регистрации
	"""

	# Проверяем, залогинен ли пользователь (смотрим сессию)
	if request.user.id:
		return redirect("/")
	# Проверяем, пришел ли запрос методом пост
	if request.method == "POST":
		# Создаем форму с пришедшими данными 
		form = NewUserForm(request.POST,request.FILES)
		# Валидируем запрос
		if form.is_valid():
			# Создаем путь и имя для аватарки
			file_name = request.POST['username'] +'_'+ request.FILES['foto'].name 
			# Сохраняем данные в таблицу пользователей
			user = form.save()
			# Проходим процедуру сохранения фотографии 
			# (в отдельной таблице хранится путь до фото у конкретного пользователя)
			last_user = User.objects.all().order_by('-id')[:1]
			Profile.objects.create(foto=file_name, 
								user_id=last_user[0].id)
			# Вызывае функцию сохранения файла
			handle_uploaded_file(request.FILES['foto'].file, file_name)
			# Залогиниваемся от вновь зарегистрированного пользователя 
			# и перенаправлеям его на страницу вопросов
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	# Если пришел не пост запрос или если данные не валидны,
	# создаем пустую форму и рендерим шаблон регистрации
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def user_login(request):
    """
    Функция валидации формы входа
    """

    # Проверяем, залогинен ли пользователь (смотрим сессию)
    if request.user.id:
    	return redirect("/")
    # Проверяем, пришел ли запрос методом пост
    if request.method == 'POST':
    	# Создаем форму с пришедшими данными 
        form = LoginForm(request.POST)
        # Валидируем запрос
        if form.is_valid():
        	# Вызываем встроенные процесс аутентификации
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            # при успешной аутентификации залогиниваемся
        	# от вновь зарегистрированного пользователя 
			# и перенаправлеям его на страницу вопросов
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
                else:
                    messages.error(request, "Disabled account")
            else:
            	messages.error(request, "Invalid login")
    else:
    	# Если пришел не пост запрос или если данные не валидны,
		# создаем пустую форму и рендерим шаблон входа
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def handle_uploaded_file(f, save_name):
	"""
	Функция сохранения аватарки при регистрации  
	"""
	f.seek(0)
	file = open(settings.AVATARS_URL+'/'+save_name, 'wb') 
	file.write(f.read())