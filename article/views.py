from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Article, Tag, Category, SubContent, SubContentImage
from .forms import CommentForm


def index(request):
    articles = Article.objects.order_by('-id')
    lists = Article.objects.order_by('-id')[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    tag = request.GET.get('tag')
    category = request.GET.get('category')
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if category:
        articles = articles.filter(category__title__exact=category)
    q = request.GET.get('q')
    if q:
        articles = articles.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 3)

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)

    context = {
        'object_list': page_obj,
        'lists': lists,
        'tags': tags,
        'categories': categories,
    }
    return render(request, 'wordify/index.html', context)


def detail_art(request, pk):
    article = get_object_or_404(Article, id=pk)
    lists = Article.objects.order_by('-id')[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    form = CommentForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(reverse('article:detail', kwargs={'pk': article.id}))
        form = CommentForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author_id = request.user.profile.id
            obj.article_id = article.id
            obj.save()
            return redirect('.')
    context = {
        'object': article,
        'form': form,
        'lists': lists,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'wordify/blog-single.html', context)
