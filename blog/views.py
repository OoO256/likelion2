from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    posts = Post.objects.all
    return render(request, 'blog/home.html', {'post_list' : posts})
    
def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
            
    return render(request, 'blog/new.html', {'form' : form })
    
def edit(request, index):
    post = get_object_or_404(Post, pk=index)
    
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/edit.html', {'post' : post, 'form' : form})

def post_detail(request,index):
    post= get_object_or_404(Post, pk=index)
    return render(request, 'blog/detail.html', {'post':post})
    
    
def delete(request, index):
    #posts = Post.objects.all
    
    post = get_object_or_404(Post, pk=index)
    post.delete()
    return redirect('home')