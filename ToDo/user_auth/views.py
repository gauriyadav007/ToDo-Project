from django.shortcuts import render, redirect
from .forms import RegisterForm, ForgotPasswordForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            full_name = form.cleaned_data['full_name']
            contact_no = form.cleaned_data['contact_no']
            # create user
            user = User.objects.create_user(username=username, email=email, password=password)
            # store full_name in first_name (simple approach)
            user.first_name = full_name # store full name
            user.save()
            # store contact in user.profile? For simplicity skip and show message
            messages.success(request, 'Registration done. Please login.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            # Check if user exists
            if not User.objects.filter(username=username).exists():
                # New user, show message to register
                messages.info(request, "You are a new user. Please register first.")
            else:
                messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')


@login_required
def logout_(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login_')


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            new_password = form.cleaned_data['new_password']
            try:
                user = User.objects.get(username=username)
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password updated. Please login with new password.')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'User not found.')
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgot_password.html', {'form': form})


@login_required
def profile(request):
    # profile shows username, email, full name (stored in first_name)
    # Show popup message using messages framework
    return render(request, 'profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes saved.")  # Success message
            return redirect('profile')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = EditProfileForm(instance=request.user)
            
    return render(request, 'edit_profile.html', {'form': form})
