from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            new_user = form.save()
            messages.info(response, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                )
            login(response, new_user)
        return redirect("/")
    else:
        form = UserCreationForm()
    return render(response, "register/register.html", {"form":form})
