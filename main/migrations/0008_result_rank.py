# Generated by Django 5.0.1 on 2024-01-30 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='rank',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
