from django.shortcuts import render, redirect, reverse
from main.models import Article, Commentary, Result, Tag, Category
from .forms import CommentForm
from django.contrib import messages
# Create your views here.


def blog_detail(request, slug):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    pid = request.GET.get("pid")
    form = CommentForm()
    article = Article.objects.get(slug=slug)
    articles = Article.objects.order_by('-id')[:3]
    if request.method == "POST":
        comment = CommentForm(request.POST, files=request.FILES)
        if comment.is_valid():
            obj = comment.save(commit=False)
            obj.article = article
            if pid:
                obj.parent_comment = Commentary.objects.get(id=pid)
            obj.save()
            messages.success(request, "Comment sent successfully")
            reverse_url = reverse('blog:detail', args=[slug])
            return redirect(reverse_url)
    ctx = {
        "article": article,
        "form": form,
        "tags": tags,
        "categories": categories,
        "articles": articles,
    }
    return render(request, 'blog/single.html', ctx)


def blog_list(request):
    articles = Article.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    print(tag)
    if cat:
        articles = Article.objects.filter(category__name__exact=cat)
    if tag:
        articles = Article.objects.filter(tag__name__exact=tag)
    ctx = {
        "articles": articles,
    }
    return render(request, 'blog/blog.html', ctx)
