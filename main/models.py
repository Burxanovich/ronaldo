from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import pre_save
from django.utils.text import slugify
import datetime

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    subject = models.CharField(max_length=225)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AboutMe(models.Model):
    image = models.ImageField(upload_to='owner/', null=True, blank=True)
    name = models.CharField(max_length=225)
    date_birth = models.DateField()
    address = models.CharField(max_length=225)
    email = models.EmailField()
    phone = PhoneNumberField(null=True, blank=True, region='UZ',  help_text='Telefon raqamini 901234567 formatida kiriting.')
    project_count = models.IntegerField(null=True, blank=True)
    awards_count = models.IntegerField(null=True, blank=True)
    happy_customers = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Partner(models.Model):
    partner = models.ForeignKey(AboutMe, on_delete=models.SET_NULL, blank=True, null=True, related_name='partners')
    image = models.ImageField(upload_to='article/partners/', null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(AboutMe, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default='another', related_name='categories', null=True, blank=True)
    tag = models.ManyToManyField(Tag, related_name='tags')
    image = models.ImageField(upload_to='article/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    name = models.CharField(max_length=225)
    message = models.TextField()
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to='article/comments/', null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="parent", null=True, blank=True)
    top_level_comment = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def children(self, *args, **kwargs):
        if not self.top_level_comment:
            child = Commentary.objects.filter(top_level_comment=self.id)
            return child
        else:
            return None


def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent_comment:
        if instance.parent_comment.top_level_comment:
            instance.top_level_comment = instance.parent_comment.top_level_comment
        else:
            instance.top_level_comment = instance.parent_comment.id


pre_save.connect(comment_pre_save, sender=Commentary)


class SubArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='sub_articles')
    title = models.CharField(max_length=225)
    content = models.TextField()
    image = models.ImageField(upload_to='article/sub_article/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def article_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title) + slugify(datetime.datetime.now().strftime("%x"))


pre_save.connect(article_pre_save, sender=Article)


class Result(models.Model):
    TYPE = (
        (0, "Experience"),
        (1, "Education"),
        (2, "Awards")
    )
    rank = models.CharField(max_length=225, null=True, blank=True)
    type = models.IntegerField(choices=TYPE)
    begin_date = models.DateField()
    finish_date = models.DateField()
    address = models.CharField(max_length=225)
    message = models.TextField()


class Service(models.Model):
    service_type = models.CharField(max_length=225)
    content = models.TextField()


class Skill(models.Model):
    LEVEL = (
        (0, "top"),
        (1, "low")
    )
    level = models.IntegerField(choices=LEVEL)
    name = models.CharField(max_length=225)
    last_week = models.IntegerField()
    last_month = models.IntegerField()
    percent = models.IntegerField()

    def __str__(self):
        return self.name


