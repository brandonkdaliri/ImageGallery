from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm

# Create your views here.
def register(response):
    # Create new user
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
            # Redirect to homepage after successful account creation
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(response, user)
            return redirect('/') 
    else:
        form = RegistrationForm()
    return render(response, 'register/register.html', {'form': form})