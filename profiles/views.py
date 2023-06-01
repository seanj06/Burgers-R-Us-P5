from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm


def profile(request):

    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile has been updated')
        else:
            messages.error(request, 'Sorry something went wrong')    

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)
