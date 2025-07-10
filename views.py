from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsArticle
from .forms import NewsArticleForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def news_list(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            articles = NewsArticle.objects.all().order_by('-publish_date')
        else:
            articles = NewsArticle.objects.filter(user=request.user).order_by('-publish_date')
    else:
        articles = NewsArticle.objects.none()  
    return render(request, 'news/list.html', {'articles': articles})

@login_required
def news_create(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.publish()
            return redirect('news_list')
    else:
        form = NewsArticleForm()
    return render(request, 'news/form.html', {'form': form})

@login_required
def news_edit(request, pk):
    if not request.user.is_staff:
        return redirect('news_list')

    article = get_object_or_404(NewsArticle, pk=pk)
    form = NewsArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        article.save()
        return redirect('news_list')
    return render(request, 'news/form.html', {'form': form})

@login_required
def news_delete(request, pk):
    if not request.user.is_staff:
        return redirect('news_list')

    article = get_object_or_404(NewsArticle, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('news_list')
    return render(request, 'news/delete.html', {'article': article})

@csrf_exempt 
def custom_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('news_list')
