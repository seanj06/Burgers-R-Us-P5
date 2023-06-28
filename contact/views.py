from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm
from .models import ContactMessage
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


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
    contact = ContactMessage.objects.latest('time')
    subject = f'Enquiry Confirmation - Enquiry {contact.subject}'
    from_email = 'burgers-r-us@example.com'
    to_email = [contact.email]

    html_message = render_to_string('contact/email/enquiry_confirmation.html',
                                    {'contact': contact})
    plain_message = strip_tags(html_message)

    send_mail(subject, plain_message,
              from_email, to_email,
              html_message=html_message)

    return render(request, 'contact/contact-success.html')
