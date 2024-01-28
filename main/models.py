from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    subject = models.CharField(max_length=225)
    message = models.TextField()

    def __str__(self):
        return self.name


class AboutMe(models.Model):
    name = models.CharField(max_length=225)
    date_birth = models.DateField()
    address = models.CharField(max_length=225)
    email = models.EmailField()
    phone = PhoneNumberField(null=True, blank=True, region='UZ',  help_text='Telefon raqamini +998901234567 formatida kiriting.')
    project_count = models.IntegerField()
    partners = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='partner')

    def __str__(self):
        return self.name






