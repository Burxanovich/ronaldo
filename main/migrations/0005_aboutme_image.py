# Generated by Django 5.0.1 on 2024-01-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_categories_category_remove_aboutme_partners_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='owner/'),
        ),
    ]
