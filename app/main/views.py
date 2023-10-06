from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import *
from main.forms import AddPostForm, AddProductForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from account.models import Profile



def index(request): #Главная  
    post_news = News.objects.filter(cat_id=1).order_by('-date')[:3]   
    context = {
        'post_news' : post_news,                     
        }    
    return render(request, 'main/index.html', context=context)

# --------------------------------------------------------------------------

def news(request): #Новости 
    post_news = News.objects.all().order_by('-date') 

    paginator = Paginator(post_news, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    cats = Category.objects.all()    
    context = {
        'post_news' : post_news,
        'cats' : cats,
        'cat_selected' : 0,
        'page_obj' : page_obj
        }
    return render(request, 'main/news.html',context=context  )

def show_category(request, cat_id): #Категория  
    post_news = News.objects.filter(cat_id=cat_id).order_by('-date') 
    cats = Category.objects.all() 

    paginator = Paginator(post_news, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'post_news' : post_news,
        'cats' : cats,
        'cat_selected' : cat_id,  
        'page_obj' : page_obj      
        }

    return render(request, 'main/news.html', context=context)


def show_news(request, news_id): #Конкретная новость
    post_news = get_object_or_404(News, pk=news_id)  
    context = {
        'post_news' : post_news,                
        }
    return render(request, 'main/show_news.html', context=context)

@login_required(login_url='log')
def add(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            
            # Определение категории на основе роли пользователя
            if request.user.is_superuser:
                # Если пользователь - суперпользователь, установите категорию "Администратор"
                category_name = "Администрация"
            else:
                # В противном случае, установите категорию "Студент"
                category_name = "Студент"
            
            # Поиск категории по имени
            category,categored = Category.objects.get_or_create(name=category_name)
            
            news.cat = category  # Установите категорию для новости
            news.author = request.user  # Установите автора новости
            news.save()
            return redirect('main:news')
    else:
        form = AddPostForm()
    
    context = {
        'form': form,         
        'text' : 'Опубликовать 💪💪💪'
    }

    return render(request, 'main/add_news.html', context)

@login_required(login_url='log')
def update_news(request, news_id):
    # Получите новость по её ID или верните 404, если не существует
    news = get_object_or_404(News, pk=news_id)

    # Проверьте, является ли текущий пользователь автором новости
    if news.author != request.user:
        # Если пользователь не является автором, вы можете выполнить нужные действия,
        # например, перенаправить пользователя на другую страницу или отобразить сообщение об ошибке.
        return HttpResponseForbidden("У вас нет разрешения на обновление этой новости.")

    if request.method == 'POST':
        # Обработайте обновление новости, используя данные из формы
        form = AddPostForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('main:show_news', news_id=news_id)
    else:
        # Отобразите форму для обновления новости
        form = AddPostForm(instance=news)
    
    context = {
        'form': form, 
        'news': news, 
        'text' : 'Обновить 💪💪💪'
    }

    return render(request, 'main/add_news.html', context)


@login_required(login_url='log')
def delete_news(request, news_id):
    # Получите новость по её ID или верните 404, если не существует
    news = get_object_or_404(News, pk=news_id)

    # Проверьте, является ли текущий пользователь автором новости
    if news.author != request.user:
        # Если пользователь не является автором, вы можете выполнить нужные действия,
        # например, перенаправить пользователя на другую страницу или отобразить сообщение об ошибке.
        return HttpResponseForbidden("У вас нет разрешения на удаление этой новости.")

    if request.method == 'POST':
        if request.POST.get("confirm_delete"):
              # Удалите новость, если пользователь подтвердил действие
              news.delete()
              
        return redirect('account:profile')  # Измените на страницу пользователя

    
    
    return render(request, 'account/profile2.html', {'news': news})

# --------------------------------------------------------------------------

def store(request): #Магазин
    product = Product.objects.all().order_by('-publication_date') 

    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    cats = Category_prod.objects.all() 
    context = {
        'product' : product,
        'cats' : cats,
        'cat_selected' : 0,
        'page_obj' : page_obj
    }
    return render(request, 'main/store.html', context=context)

def show_card(request,card_id):
    card = get_object_or_404(Product, pk=card_id)
    context = {
        'card' : card,
    }
    return render(request, 'main/show_card.html', context=context)

def show_prod_category(request, cat_id):
    product = Product.objects.filter(cat_prod_id=cat_id)
    cats = Category_prod.objects.all()
    context = {
        'product' : product,
        'cats' : cats,
        'cat_selected' : cat_id,  
    }
    return render(request, 'main/store.html', context=context)

@login_required(login_url='log')
def create_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('main:store')
    else:
        form = AddProductForm()

    context = {
        'form': form, 
        'text' : 'Опубликовать 💪💪💪'
    }
    return render(request, 'main/add_prod.html', context)


@login_required(login_url='log')
def update_prod(request, card_id):
    # Получите товар по её ID или вернёт 404, если не существует
    product = get_object_or_404(Product, pk=card_id)

    # Проверьте, является ли текущий пользователь автором товара
    if product.author != request.user:
        # Если пользователь не является автором, вы можете выполнить нужные действия,
        # например, перенаправить пользователя на другую страницу или отобразить сообщение об ошибке.
        return HttpResponseForbidden("У вас нет разрешения на обновление этого товара.")

    if request.method == 'POST':
        # Обработайте обновление новости, используя данные из формы
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('main:show_card', card_id=card_id)
    else:
        # Отобразите форму для обновления новости
        form = AddProductForm(instance=product)
    
    context = {
        'form': form, 
        'product': product, 
        'text' : 'Обновить 💪💪💪'
    }

    return render(request, 'main/add_prod.html', context)


@login_required(login_url='log')
def delete_prod(request, card_id):
    # Получите новость по её ID или верните 404, если не существует
    product = get_object_or_404(Product, pk=card_id)

    # Проверьте, является ли текущий пользователь автором новости
    if product.author != request.user:
        # Если пользователь не является автором, вы можете выполнить нужные действия,
        # например, перенаправить пользователя на другую страницу или отобразить сообщение об ошибке.
        return HttpResponseForbidden("У вас нет разрешения на удаление этого товара.")

    if request.method == 'POST':
        if request.POST.get("confirm_delete"):
              # Удалите новость, если пользователь подтвердил действие
              product.delete()
              
        return redirect('account:profile')  # Измените на страницу пользователя

    
    
    return render(request, 'account/profile2.html', {'product': product})

# --------------------------------------------------------------------------


