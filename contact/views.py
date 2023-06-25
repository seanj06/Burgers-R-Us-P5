from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm
from django.contrib.auth.decorators import login_required


@login_required
def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.user = request.user
            contact_message.save()
            messages.success(request, 'Your enquiry has been sent')
            return redirect('contact_success')
    else:
        form = ContactMessageForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request):
    """
    View to render contact success page
    """
    return render(request, 'contact/contact-success.html')
