from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        print("False")
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
