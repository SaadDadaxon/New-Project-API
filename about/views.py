from django.shortcuts import render
from .models import About


def about(request):
    feedbacks = About.objects.all()
    context = {
        'feedbacks': feedbacks
    }
    return render(request, 'wordify/about.html', context)
