from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import Post

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def admin(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content, created_by=request.user)
        return redirect('user_post')
    return render(request, 'accounts/admin.html')

def user(request):
    posts = Post.objects.all()
    return render(request, 'accounts/user.html', {'posts': posts}) 
