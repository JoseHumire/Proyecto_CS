from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
        ]
        labels = {
            'email': 'Email address',
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Repeat Password',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProfessionalForm(forms.ModelForm):

    class Meta:
        model = Professional
        fields = ['city', 'professions', 'phone', 'id_number', 'status']
        labels = {
            'city': 'City',
            'professions': 'Profession',
            'phone': 'Phone number',
            'id_number': 'ID Number',
            'status': 'Status',
        }
        widgets = {
            'city': forms.Select(attrs={'class': 'form-control'}),
            'professions': forms.CheckboxSelectMultiple(),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = [
            'profession', 'description', 'start_date', 'finish_date'
        ]
        labels = {
            'profession': 'Profession',
            'description': 'Description',
            'start_date': 'Start Date',
            'finish_date': 'Finish Date',
        }
        widgets = {
            'profession': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'finish_date': forms.DateTimeInput(
                attrs={'class': 'form-control'}),
        }


class StudyForm(forms.ModelForm):

    class Meta:
        model = Study
        fields = [
            'school', 'profession', 'name'
        ]
        labels = {
            'school': 'Institution',
            'profession': 'Profession',
            'name': 'Degree',
        }
        widgets = {
            'school': forms.Select(attrs={'class': 'form-control'}),
            'profession': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
