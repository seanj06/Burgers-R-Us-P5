from django.shortcuts import render
from django.contrib import messages
from .forms import ContactMessageForm


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your form has been submitted,\
                     we will be in touch shortly'
                )
            return redirect('home')
    else:
        form = ContactMessageForm()

    return render(request, 'contact/contact.html')
