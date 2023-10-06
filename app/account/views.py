from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from main.models import News, Product
from account.models import Profile
from account.forms import RegisterUserForm, ProfileEditForm



def profile(request): #Профиль
    user_news = News.objects.filter(author=request.user).order_by('-date') 
    user_product = Product.objects.filter(author=request.user).order_by('-publication_date') 
    user_prof = Profile.objects.get(user=request.user)       

    context = {
        'user_news': user_news,
        'user_product' : user_product,
        'user_prof' : user_prof,

        }
    return render(request, 'account/profile2.html', context)

@login_required(login_url='log')
def edit_profile(request):
    user_prof = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=user_prof)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен.')
            return redirect('account:profile')
        else:
            messages.error(request, 'Исправьте ошибки в форме.')

    else:
        form = ProfileEditForm(instance=user_prof)

    context = {
        'form': form,
        'user_prof': user_prof,
    }

    return render(request, 'account/edit_profile.html', context)

def log(request): # Авторизация
    user_auth_failed = False  # Флаг для отслеживания неудачной аутентификации

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            post_news = News.objects.filter(cat_id=1).order_by('-date')[:3]  
            
            context = {
                'post_news': post_news,                
            }            

            return render(request, 'main/index.html', context)
        else:
            user_auth_failed = True  # Устанавливаем флаг неудачной аутентификации
            messages.error(request, 'Неверное имя пользователя или пароль')
    
    return render(request, 'registration/login.html', {'user_auth_failed': user_auth_failed})


def reg(request): #Регестрация

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()            
            messages.success(request, 'Регистрация прошла успешно. Теперь вы можете войти.')
            return redirect('account:log')
        else:
            # В случае ошибок валидации, форма будет содержать ошибки
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Ошибка в поле "{field}": {error}')
    else:
        form = RegisterUserForm()

    return render(request, 'registration/reg.html', {'form': form})

@login_required(login_url="/")
def logout_user(request):
    logout(request)
    messages.warning(request, ("Вы вышли из аккаунта"))
    return redirect("main:index")

