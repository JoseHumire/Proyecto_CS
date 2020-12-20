import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from django.contrib.auth.models import User
from django.utils import timezone


class Country(TranslatableModel):

    translations = TranslatedFields(
        name=models.CharField(max_length=40, verbose_name=_('Name'))
    )
    creation_date = models.DateTimeField(
        default=timezone.now, verbose_name=_("Creation Date"))

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name


class City(TranslatableModel):
    country = models.ForeignKey(
        Country,
        related_name='cities',
        on_delete=models.CASCADE,
        verbose_name=_('Country')
    )

    translations = TranslatedFields(
        name=models.CharField(max_length=50, verbose_name=_('Name'))
    )

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.name


class School(TranslatableModel):

    translations = TranslatedFields(
        name=models.CharField(max_length=200, verbose_name=_('Name'))
    )
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, verbose_name=_('City'))

    class Meta:
        verbose_name = _('School')
        verbose_name_plural = _('Schools')

    def __str__(self):
        return self.name


class Profession(TranslatableModel):

    translations = TranslatedFields(
        name=models.CharField(max_length=50, verbose_name=_('Name')),
        description=models.CharField(
            max_length=200, default='', verbose_name=_('Description'))
    )

    class Meta:
        verbose_name = _('Profession')
        verbose_name_plural = _('Professions')

    def __str__(self):
        return self.name


class Professional(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=_('User'))
    city = models.ForeignKey(
        City,
        related_name=_('professionals'),
        on_delete=models.CASCADE,
        default='',
        verbose_name=_('City')
    )
    professions = models.ManyToManyField(
        Profession, verbose_name=_('Professions'))
    phone = models.CharField(
        max_length=9, default='', verbose_name=_('Phone'))
    id_number = models.CharField(
        max_length=11, default='', verbose_name=_('Id Number'))
    id_image = models.ImageField(
        null=False, blank=True, verbose_name=_('Id Image'))
    status = models.BooleanField(default=True, verbose_name=_('Status'))
    birthdate = models.DateField(
        default=datetime.date.today, verbose_name=_('Birthdate'))
    creation_date = models.DateTimeField(
        default=timezone.now, verbose_name=_('Creation Date'))
    profile_picture = models.ImageField(
        null=True, blank=True, verbose_name=_('Profile Picture'))

    class Meta:
        verbose_name = _('Professional')
        verbose_name_plural = _('Professionals')

    def __str__(self):
        return self.user.get_username()


class Curriculum(models.Model):
    owner = models.OneToOneField(
        Professional, on_delete=models.CASCADE, verbose_name=_('Owner'))
    contract_price = models.IntegerField(
        default=0, verbose_name=_('Contract price'))
    score = models.IntegerField(default=5, verbose_name=_('Score'))

    class Meta:
        verbose_name = _('Curriculum')
        verbose_name_plural = _('Curriculums')

    def __str__(self):
        return self.owner.user.get_username() + '-cv'


class Job(models.Model):

    cv = models.ForeignKey(
        Curriculum,
        related_name=_('jobs'),
        on_delete=models.CASCADE
    )
    profession = models.ForeignKey(
        Profession, on_delete=models.CASCADE, verbose_name=_('Profession'))
    description = models.TextField(
        max_length=500, default='', verbose_name=_('Description'))
    start_date = models.DateTimeField(
        default=timezone.now, verbose_name=_('Start Date'))
    finish_date = models.DateTimeField(
        default=timezone.now, verbose_name=_('Finish Date'))

    class Meta:
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')

    def __str__(self):
        return self.profession.name


class JobOffer(models.Model):
    user = models.ForeignKey(
        Professional,
        related_name='job_offers',
        on_delete=models.CASCADE,
        verbose_name=_('User')
    )
    city = models.ForeignKey(
        City,
        related_name='job_offers',
        on_delete=models.CASCADE, default='',
        verbose_name=_('City')
    )

    description = models.CharField(
        max_length=100, default='', verbose_name=_('Description'))
    creation_date = models.DateTimeField(
        default=timezone.now, verbose_name=_('Creation Date'))
    status = models.BooleanField(default=True, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Job Offer')
        verbose_name_plural = _('Job Offers')


class Employment(models.Model):
    offer = models.ForeignKey(
        JobOffer,
        related_name='employments',
        on_delete=models.CASCADE,
        verbose_name=_('Offer')
    )
    profession = models.ForeignKey(
        Profession, on_delete=models.CASCADE, verbose_name=_('Profession'))
    description = models.TextField(
        max_length=200, default='', verbose_name=_('Description'))
    reward = models.FloatField(default=0, verbose_name=_('Reward'))
    status = models.BooleanField(default=True, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Employment')
        verbose_name_plural = _('Employments')


class Study(models.Model):
    cv = models.ForeignKey(
        Curriculum,
        related_name='studies',
        on_delete=models.CASCADE
    )
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, verbose_name=_('School')
    )
    profession = models.ForeignKey(
        Profession, on_delete=models.CASCADE, verbose_name=_('Profession')
    )
    name = models.CharField(max_length=100, default='', verbose_name=_('Name'))
    image = models.ImageField(null=False, blank=True, verbose_name=_('Image'))

    class Meta:
        verbose_name = _('Study')
        verbose_name_plural = _('Studies')


class ChatRoom(models.Model):
    users = models.ManyToManyField(Professional, verbose_name=_('Users'))
    creation_date = models.DateTimeField(
        default=timezone.now, verbose_name=_('Creation Date')
    )
    status = models.BooleanField(default=True, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Chat Room')
        verbose_name_plural = _('Chat Rooms')

    @staticmethod
    def get_room(user, other_user):
        room = ChatRoom.objects.filter(users__in=[user]).filter(
            users__in=[other_user]).first()
        return room

    def get_other_user(self, user):
        users = self.users.all()
        other_user = users[0]
        if users[0] == user:
            other_user = users[1]
        return other_user

    def has_user(self, user):
        users = self.users.all()
        return user == users[0] or user == users[1]


class Message(models.Model):
    class Meta:
        ordering = ['creation_date']
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    chat_room = models.ForeignKey(
        ChatRoom, on_delete=models.CASCADE, verbose_name=_('Chat Room'))
    user = models.ForeignKey(
        Professional, on_delete=models.CASCADE, verbose_name=_('User'))
    message = models.CharField(
        max_length=400, verbose_name=_('Message'))
    creation_date = models.DateTimeField(
        default=timezone.now, verbose_name=_('Creation Date'))
