from django.shortcuts import render,get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, BlogPostForm
from .models import BlogPost


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog.html', {'form': form})

def home_view(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'blogs': blogs})


def blog_detail(request,blog_id):
    blog=get_object_or_404(BlogPost,id=blog_id)
    return render(request,'blog_detail.html',{'blog':blog})

def view_all_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')  # Get all blogs sorted by newest first
    return render(request, 'view_blogs.html', {'blogs': blogs})