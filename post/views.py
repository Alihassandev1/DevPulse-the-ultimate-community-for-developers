from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from . import forms
from .models import Post
from django.contrib.auth import get_user_model
# Create your views here.

def posthome(request):
    query = request.GET.get('q', '').strip()
    post = Post.objects.all()
    userProfile = None
    
    if query:
        # Find all users matching the query
        userProfile = get_user_model().objects.filter(username__icontains=query)
        
        if userProfile.exists():
            # If username matches found, show posts by those users
            post = post.filter(creator__in=userProfile)
        else:
            # If no username match, search by content
            post = post.filter(Q(content__icontains=query))
    
    post = post.order_by('-created_at')
    return render(request, 'post/posthome.html', {'post': post, 'search_query': query, 'showSearch' : False, 'userProfile': userProfile})

@login_required
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
    profile_user = get_user_model().objects.get(username=username)
    
    # Handle AJAX image upload
    if request.method == 'POST' and request.FILES.get('profile_image'):
        if request.user.is_authenticated and request.user == profile_user:
            try:
                # Access profile_data with safe attribute check
                if hasattr(profile_user, 'profile_data'):
                    profile_data = profile_user.profile_data
                    profile_data.img = request.FILES['profile_image']
                    profile_data.save()
                    return JsonResponse({'status': 'success', 'message': 'Image uploaded successfully', 'image_url': profile_data.img.url})
                else:
                    return JsonResponse({'status': 'error', 'message': 'User profile not found'}, status=400)
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=403)
    
    post = Post.objects.filter(creator=profile_user)
    recent_posts = Post.objects.filter(creator=profile_user).order_by('-created_at')[:5]
    return render(request, 'post/profile.html', {'post': post, 'recent_posts': recent_posts, 'profile': profile_user})
