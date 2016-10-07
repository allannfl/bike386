from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
	return render(request,"index.html")
	
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            from django.contrib.auth import authenticate, login
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html')

@login_required
def eventos(request):
    return render(request, 'eventos.html')

def sobre(request):
	return render(request, 'sobre.html')

@login_required
def galeria(request):
	return render(request, 'galeria.html')

def contato(request):
	return render(request, 'contato.html')

