from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden, HttpResponse
from django.template import loader
from django.views.generic.edit import FormView

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
        user_form = UserForm(data=request.POST)
        professional_form = ProfessionalForm(data=request.POST)
        if user_form.is_valid() and professional_form.is_valid():
            user = user_form.save()
            professional = professional_form.save(commit=False)
            professional.user = user
            professional.save()
            Curriculum.objects.create(owner=professional)
            return redirect('login')

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
                return redirect('/home')

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

# Mensajes
def pantallaprincipal(request):
    return render(request, "pantallaprincipal.html")

# Mensajes
def prueba(request):
    return render(request, "prueba.html")

def user_profile(request):
    current_user = request.user
    professional = Professional.objects.get(user=current_user)
    professions = professional.professions.all()
    template = loader.get_template('users/profile.html')
    context = {
        'user': current_user,
        'professional': professional,
        'professions': professions,
    }
    return HttpResponse(template.render(context, request))


def add_job(request, pk=None):
    if pk:
        job = get_object_or_404(Job, pk=pk)
        if job.cv.owner.user != request.user:
            return HttpResponseForbidden()
    else:
        cv = Curriculum.objects.get(owner=request.user.professional)
        job = Job(cv=cv)
    form = JobForm(data=request.POST or None, instance=job)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(
        request, "add_job.html", {'form': form}
    )


def add_study(request, pk=None):
    if pk:
        study = get_object_or_404(Study, pk=pk)
        if study.cv.owner.user != request.user:
            return HttpResponseForbidden()
    else:
        cv = Curriculum.objects.get(owner=request.user.professional)
        study = Study(cv=cv)
    form = StudyForm(data=request.POST or None, instance=study)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(
        request, "add_study.html", {'form': form}
    )


def employments(request):
    return render(request, "employments.html")

def index(request):
    return render(request, "index.html")

def my_posts(request):
    return render(request, "my_posts.html")

def create_job_offer(request):
    offer_form = JobOfferForm()
    employment_formset = EmploymentInlineFormSet()
    if request.method == 'POST':
        offer_form = JobOfferForm(data=request.POST)
        if offer_form.is_valid():
            offer = offer_form.save(commit=False)
            professional = Professional.objects.get(user=request.user)
            offer.user = professional
            offer.save()
            employment_formset = EmploymentInlineFormSet(
                data=request.POST, instance=offer
            )
            if employment_formset.is_valid():
                employment_formset.save()
            print(employment_formset.errors)
            return redirect('home')

    return render(
        request,
        "create_offer.html",
        {
            'offer_form': offer_form,
            'employment_formset': employment_formset
        }
    )


def job_offer(request, offer_id):
    offer_list = JobOffer.objects.all()
    current_offer = JobOffer.objects.get(pk=offer_id)
    context = {
        'offers': offer_list,
        'offer': current_offer,
    }
    return render(request, 'offers.html', context)


