from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import User
from .forms import UserForm, UserProfileForm


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    if not User.objects.filter(email=request.user.email).exists():
        User.objects.create(
            first_name=request.user.first_name,
            last_name=request.user.last_name,
            email=request.user.email)

    return render(request, 'home.html', {'media': settings.MEDIA_URL})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = UserProfileForm(instance=request.user.userprofile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
        return render(request,
                      'edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})


@login_required
def all_users(request):
    users = User.objects.all()
    return render(request, 'all.html', {
        'users': users,
        'media': settings.MEDIA_URL,
    })
