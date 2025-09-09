from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RegisterForm, LoginForm, RequestForm
from .models import Request

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Добро пожаловать!')
                return redirect('profile')
            else:
                messages.error(request, 'Неверные данные')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы.')
    return redirect('home')

def home_view(request):
    return render(request, 'home.html')

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user_requests = Request.objects.filter(user=request.user)
    return render(request, 'profile.html', {'requests': user_requests})

def create_request_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.user = request.user
            request_obj.save()
            messages.success(request, 'Заявка создана!')
            return redirect('profile')
    else:
        form = RequestForm()
    
    return render(request, 'create_request.html', {'form': form})

def delete_request_view(request, request_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    request_obj = get_object_or_404(Request, id=request_id, user=request.user)
    request_obj.delete()
    messages.success(request, 'Заявка удалена')
    return redirect('profile')

@staff_member_required
def admin_dashboard(request):
    all_requests = Request.objects.all().order_by('-created_at')
    return render(request, 'admin_dashboard.html', {'requests': all_requests})