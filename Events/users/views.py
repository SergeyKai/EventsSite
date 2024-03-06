from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    ctx = {
        'form': UserCreationForm()
    }

    return render(request, 'users/registration.html', context=ctx)


def profile(request):
    return render(request, 'users/profile.html')
