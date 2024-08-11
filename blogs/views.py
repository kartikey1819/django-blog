from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category

def posts_by_category(request, category_id):
    # Fetch posts belonging to the given category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    # use try/except when we want to do some custom action if the category does not exists
    try:
        category = Category.objects.get(pk=category_id)
    except:
        # redirect the user to homepage
        return redirect('home')
    #use get_object_or_404 when you want to show 404 error page if the category does not exist
    # category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)