from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm


def profile(request):
    
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)
