from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('title')
    return render(request, 'infpoolsite/post_list.html', {'posts':posts})