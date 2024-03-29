# Generated by Django 5.0.1 on 2024-01-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_commentary_top_level_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'Experience'), (1, 'Education'), (2, 'Awards')])),
                ('begin_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('address', models.CharField(max_length=225)),
                ('message', models.TextField()),
            ],
        ),
    ]
