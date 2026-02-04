from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your views here.

def posthome(request):
    if request.user.is_authenticated:
        post = Post.objects.all().order_by('-created_at')
        return render(request, 'post/posthome.html', {'post': post})
    else:
        return redirect('user:login')

@login_required(login_url='user:login')
def newPost(request):
    form = forms.CreatePost()
    if request.method == 'POST':    
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.save()
            return redirect('post:posthome')
    return render(request, 'post/newpost.html', {'form': form})

def postView(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/postview.html', {'post': post})

def profile(request, username):
    profile = get_user_model().objects.get(username=username)
    post = Post.objects.filter(creator=profile)
    recent_posts = Post.objects.filter(creator=profile).order_by('-created_at')[:5]
    return render(request, 'post/profile.html', {'post': post, 'recent_posts': recent_posts, 'profile': profile})