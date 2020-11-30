from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import *


def welcome(request):
    if request.user.is_authenticated:
        return render(request, "users/welcome.html")
    return redirect('login')


def register(request):
    user_form = UserForm()
    professional_form = ProfessionalForm()
    user_form.fields['username'].help_text = None
    user_form.fields['password1'].help_text = None
    user_form.fields['password2'].help_text = None
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        user_form = UserCreationForm(data=request.POST)
        professional_form = ProfessionalForm(data=request.POST)
        # Si el formulario es válido...
        if user_form.is_valid() and professional_form.is_valid():
            # Creamos la nueva cuenta de usuario
            user = user_form.save()
            professional = professional_form.save(commit=False)
            professional.user = user
            professional.save()
            # Si el usuario se crea correctamente
            return redirect('login')

    # Si llegamos al final renderizamos el formulario
    return render(
        request,
        "users/register.html",
        {
            'user_form': user_form,
            'professional_form': professional_form
        }
    )


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(
        request, "users/login.html", {'form': form}
    )


def logout(request):
    do_logout(request)
    return redirect('/')


# Pantalla principal
def home(request):
    return render(request, "home.html")


# Mensajes
def messages(request):
    return render(request, "messages.html")