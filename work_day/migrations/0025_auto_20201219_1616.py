# Generated by Django 3.1.2 on 2020-12-19 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work_day', '0024_auto_20201218_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='users',
            field=models.ManyToManyField(to='work_day.Professional', verbose_name='Users'),
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='work_day.country', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='contract_price',
            field=models.IntegerField(default=0, verbose_name='Contract price'),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='work_day.professional', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='score',
            field=models.IntegerField(default=5, verbose_name='Score'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employments', to='work_day.joboffer', verbose_name='Offer'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_day.profession', verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='reward',
            field=models.FloatField(default=0, verbose_name='Reward'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='job',
            name='finish_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Finish Date'),
        ),
        migrations.AlterField(
            model_name='job',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_day.profession', verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='job_offers', to='work_day.city', verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_offers', to='work_day.professional', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='chat_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_day.chatroom', verbose_name='Chat Room'),
        ),
        migrations.AlterField(
            model_name='message',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=400, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_day.professional', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='professionals', to='work_day.city', verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='id_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Id Image'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='id_number',
            field=models.CharField(default='', max_length=11, verbose_name='Id Number'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='phone',
            field=models.CharField(default='', max_length=9, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='professions',
            field=models.ManyToManyField(to='work_day.Profession', verbose_name='Professions'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='school',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_day.city', verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='study',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='study',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='study',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_day.profession', verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='study',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_day.school', verbose_name='School'),
        ),
    ]
