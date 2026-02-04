from django.shortcuts import render
from django.contrib.auth import get_user_model
from post.models import Post

app_name = "devpulse"

def home(request):
    return render(request, "home.html")

# def profile(request, username):
#     profile = get_user_model().objects.get(username=username)
#     user_posts = Post.objects.filter(creator=profile)
#     recent_posts = Post.objects.filter(creator=profile).order_by('-created_at')[:5]
#     return render(request, 'post/profile.html', {'user_posts': user_posts, 'recent_posts': recent_posts, 'profile': profile})