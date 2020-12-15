from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_date')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('country', 'name')


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('city', 'name')


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'phone', 'id', 'status', 'creation_date')


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('owner', 'contract_price', 'score')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'description', 'cv', 'profession', 'start_date', 'finish_date'
    )


@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'description', 'creation_date', 'status')


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('offer', 'profession', 'description', 'reward', 'status')


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ('cv', 'school', 'profession', 'name')


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('creation_date', 'status')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat_room', 'user', 'message', 'creation_date')
