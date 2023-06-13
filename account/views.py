from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('todo:index_view')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            messages.success(
                request, "Uğurla qeydiyyatdan keçildi. İndi giriş edə bilərsən.")
            return redirect('account:login_view')
    else:
        form = RegisterForm()

    context = {
        "form": form,
    }

    return render(request, 'account/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('todo:index_view')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(
                request, "Giriş uğurlu oldu!")
            return redirect('todo:index_view')
    else:
        form = LoginForm()

    context = {
        "form": form,
    }

    return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('account:login_view')
