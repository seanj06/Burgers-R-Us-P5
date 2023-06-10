from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.user = request.user
            contact_message.save()
            messages.success(request, 'Your form has been submitted.\
                 We will be in touch shortly.')
            return redirect('home')
    else:
        form = ContactMessageForm()

    context = {
        'form': form,
    }    

    return render(request, 'contact/contact.html', context)
