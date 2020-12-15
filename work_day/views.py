from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden, HttpResponse
from django.template import loader
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from .forms import *
from .filters import ProfessionalFilter


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
        professional_form = ProfessionalForm(
            data=request.POST, files=request.FILES
        )
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
    template = loader.get_template('users/login.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def logout(request):
    do_logout(request)
    return redirect('/')


@login_required(login_url='/login')
def home(request):
    try:
        offers = JobOffer.objects.filter(
            employments__profession__name__contains=
            request.user.professional.professions.all()[0]
        ).distinct()
    except IndexError:
        professional = Professional.objects.get(user=request.user)
        offers = JobOffer.objects.filter(
            city=professional.city
        )
    template = loader.get_template('home.html')
    context = {
        'offers': offers
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def messages(request):
    return render(request, "messages.html")

# Mensajes
def pantallaprincipal(request):
    return render(request, "pantallaprincipal.html")

# Mensajes
def prueba(request):
    return render(request, "prueba.html")

# Mensajes
def nuevoprincipal(request):
    return render(request, "nuevoprincipal.html")

@login_required(login_url='/login')
def user_profile(request, pk=None):
    if pk:
        current_user = User.objects.get(pk=pk)
    else:
        current_user = request.user
    professional = Professional.objects.get(user=current_user)
    professions = professional.professions.all()
    cv = Curriculum.objects.get(owner=professional)
    studies = cv.studies.all()
    jobs = cv.jobs.all()
    template = loader.get_template('users/profile.html')
    context = {
        'user': current_user,
        'professional': professional,
        'professions': professions,
        'cv': cv,
        'studies': studies,
        'jobs': jobs,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def view_professionals(request):
    professionals = Professional.objects.all()
    template = loader.get_template('professionals.html')
    professional_filter = ProfessionalFilter(
        request.GET, queryset=professionals
    )
    professionals = professional_filter.qs
    context = {
        'professionals': professionals,
        'filter': professional_filter,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def add_study(request, pk=None):
    if pk:
        study = get_object_or_404(Study, pk=pk)
        if study.cv.owner.user != request.user:
            return HttpResponseForbidden()
    else:
        cv = Curriculum.objects.get(owner=request.user.professional)
        study = Study(cv=cv)
    form = StudyForm(
        data=request.POST or None,
        instance=study,
        files=request.FILES
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    if pk:
        return render(
            request, "add_study.html", {'form': StudyForm(instance=study)}
        )
    else:
        return render(request, "add_study.html", {'form': form})


@login_required(login_url='/login')
def employments(request):
    return render(request, "employments.html")


def index(request):
    return render(request, "index.html")


@login_required(login_url='/login')
def my_posts(request):
    current_user = request.user
    professional = Professional.objects.get(user=current_user)
    offers = professional.job_offers.all()
    template = loader.get_template('my_posts.html')
    context = {
        'offers': offers,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def create_job_offer(request, pk=None):
    if pk:
        offer = get_object_or_404(JobOffer, pk=pk)
        if offer.user.user != request.user:
            return HttpResponseForbidden()
    else:
        offer = JobOffer(user=request.user.professional)
    offer_form = JobOfferForm(data=request.POST or None, instance=offer)
    employment_formset = EmploymentInlineFormSet(data=request.POST or None, instance=offer)
    if request.method == 'POST':
        if offer_form.is_valid():
            offer.save()
            if employment_formset.is_valid():
                employment_formset.save()
            return redirect('home/')

    return render(
        request,
        "create_offer.html",
        {
            'offer_form': offer_form,
            'employment_formset': employment_formset
        }
    )


@login_required(login_url='/login')
def job_offer(request, offer_id=None):
    offer_list = JobOffer.objects.all()
    if offer_id:
        current_offer = JobOffer.objects.get(pk=offer_id)
    else:
        current_offer = JobOffer.objects.all().first()

    context = {
        'offers': offer_list,
        'offer': current_offer,
    }
    return render(request, 'offers.html', context)


@login_required(login_url='/login')
def edit_profile(request):
    user_form = EditUserForm(
        data=request.POST or None,
        instance=request.user,
    )
    professional_form = ProfessionalForm(
        data=request.POST or None,
        instance=request.user.professional,
        files=request.FILES
    )
    if request.method == 'POST':
        if user_form.is_valid() and professional_form.is_valid():
            user_form.save()
            professional_form.save()
            return redirect('home')
    context = {
        'user_form': user_form,
        'professional_form': ProfessionalForm(
            instance=request.user.professional),
    }
    return render(request, 'users/edit_profile.html', context)

