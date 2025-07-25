from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from users.forms import UserRegisterForm, UserLoginForm


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('users:profile')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/signup.html', {'form': form,})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('users:profile')

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('users:profile')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})

@login_required(login_url='users:login')
def profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})


@login_required(login_url='users:login')
def user_logout(request):
    logout(request)
    return redirect('users:login')


@login_required(login_url='users:login')
def profile_edit(request):
    user = request.user
    return render(request, 'users/profile_edit.html', {'user': user})