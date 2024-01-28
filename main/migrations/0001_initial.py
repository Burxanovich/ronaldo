# Generated by Django 5.0.1 on 2024-01-28 11:16

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=225)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('date_birth', models.DateField()),
                ('address', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Telefon raqamini +998901234567 formatida kiriting.', max_length=128, null=True, region='UZ')),
                ('project_count', models.IntegerField()),
                ('partners', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partner', to='main.aboutme')),
            ],
        ),
    ]
