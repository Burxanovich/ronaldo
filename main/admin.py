from django.contrib import admin
from .models import (
    Contact,
    Commentary,
    Article,
    SubArticle,
    Category,
    Tag,
    AboutMe,
    Partner,
    Result,
    Service,
    Skill
)
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    readonly_fields = ['created_date', ]


class SubArticleInline(admin.TabularInline):
    model = SubArticle
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'category', 'created_date']
    list_display_links = ['id', 'author', 'title', 'category']
    readonly_fields = ['created_date', 'slug']
    search_fields = ['title']
    date_hierarchy = 'created_date'
    inlines = [SubArticleInline]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date']
    search_fields = ['name']
    readonly_fields = ['created_date', ]


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['id', 'name',]
    search_fields = ['name', ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    search_fields = ['name', ]


class PartnerInline(admin.TabularInline):
    model = Partner
    extra = 1


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_birth', 'email']
    inlines = [PartnerInline]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', "address")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_type', ]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'level', 'name']
