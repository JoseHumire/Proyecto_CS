import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Country(models.Model):
    name = models.CharField(max_length=40)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class School(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default='')
    professions = models.ManyToManyField(Profession)
    phone = models.CharField(max_length=9, default='')
    id_number = models.CharField(max_length=11, default='')
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.get_username()


class Curriculum(models.Model):
    owner = models.OneToOneField(Professional, on_delete=models.CASCADE)
    contract_price = models.IntegerField(default=0)
    score = models.IntegerField(default=5)


class Job(models.Model):
    cv = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    profession = models.OneToOneField(Profession, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, default='')
    start_date = models.DateTimeField(default=timezone.now)
    finish_date = models.DateTimeField(default=timezone.now() + datetime.timedelta(days=1))

    def __str__(self):
        return self.profession.name


class JobOffer(models.Model):
    user = models.ForeignKey(Professional, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default='')
    description = models.CharField(max_length=100, default='')
    creation_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)


class Employment(models.Model):
    offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    profession = models.OneToOneField(Profession, on_delete=models.CASCADE)
    description = models.TextField(max_length=200, default='')
    reward = models.FloatField(default=0)
    status = models.BooleanField(default=True)


class Study(models.Model):
    cv = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')


class ChatRoom(models.Model):
    users = models.ManyToManyField(Professional)
    creation_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)


class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(Professional, on_delete=models.CASCADE)
    message = models.CharField(max_length=400)
    creation_date = models.DateTimeField(default=timezone.now)
