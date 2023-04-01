from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_views(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact:index')
    context = {
        'form': form
    }
    return render(request, 'wordify/contact.html', context)
