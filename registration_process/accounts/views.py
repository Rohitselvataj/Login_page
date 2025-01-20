from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUser, AdminUpdateForm, LoginForm
from .models import AdminUpdate

def register(request):
    if request.method == 'POST':
        form = CustomUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUser()
    return render(request, 'accounts/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def dashboard(request):
    updates = AdminUpdate.objects.all()
    return render(request, 'accounts/dashboard.html', {'updates': updates})

@login_required
def admin_update(request):
    if not request.user.is_admin:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = AdminUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AdminUpdateForm()
    return render(request, 'accounts/admin_update.html', {'form': form})
