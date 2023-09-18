from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


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

def add(request): 
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = AddPostForm()

    
    return render(request, 'main/add_news.html', {'form':form })

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

# --------------------------------------------------------------------------

def profile(request): #Профиль
    return render(request, 'main/profile.html')

def log(request): #Авторизация
    return render(request, 'registration/login.html')

def reg(request): #Авторизация
    return render(request, 'registration/login.html')













