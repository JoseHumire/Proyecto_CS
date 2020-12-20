# Generated by Django 3.1.2 on 2020-11-27 22:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('work_day', '0003_auto_20201126_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='professional',
            name='ruc',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='contract_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='score',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='employment',
            name='reward',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='employment',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='id_number',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='professional',
            name='phone',
            field=models.CharField(default='', max_length=9),
        ),
        migrations.AddField(
            model_name='professional',
            name='professions',
            field=models.ManyToManyField(to='work_day.Profession'),
        ),
        migrations.AddField(
            model_name='professional',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 22, 15, 29, 539038, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_day.city')),
            ],
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_day.country'),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='work_day.city'),
        ),
        migrations.AddField(
            model_name='professional',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='work_day.city'),
        ),
    ]
