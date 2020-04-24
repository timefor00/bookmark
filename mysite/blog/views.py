from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
	posts = Post.objects.all
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = Post.objects.filter(pk=pk).first()
	return render(request, 'blog/post_detail.html', {'post': post})