from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import (
    Contact,
    Commentary,
    Category,
    Tag,
    Article,
    AboutMe,
    Partner,
    Result,
    Service,
    Skill,
)
from django.contrib import messages
# Create your views here.


def home_view(request):
    services = Service.objects.all()
    results = Result.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    about = AboutMe.objects.order_by('-id')[0]
    articles = Article.objects.all()
    skills = Skill.objects.all()
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Contact sent successfully")
            return redirect('/')
    ctx = {
        "form": form,
        'about': about,
        "articles": articles,
        "tags": tags,
        "categories": categories,
        "results": results,
        "services": services,
        "skills": skills
    }
    return render(request, 'main/index.html', ctx)

