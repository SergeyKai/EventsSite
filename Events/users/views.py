from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserChangeForm

from .forms import CustomUserCreationForm, CustomUserChangeForm


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    ctx = {
        'form': CustomUserCreationForm()
    }

    return render(request, 'users/registration.html', context=ctx)


def user_change(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            print(111)
            form.save()
            return redirect('profile')

    ctx = {
        'form': CustomUserChangeForm(instance=request.user)
    }

    return render(request, 'users/user_change.html', context=ctx)


def profile(request):
    return render(request, 'users/profile.html')
