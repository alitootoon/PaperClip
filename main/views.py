from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from .Form import UserForm, MediaForm
from .core import core

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'page/login.html')
    else:
        form = MediaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            media = form.save(commit=False)
            media.user = request.user
            media.data_file = request.FILES['data_file']
            file = media.data_file.url.splite('.')[-1]
            file = file.lower()

            if file not in IMAGE_FILE_TYPES:
                context = {
                    'from': form,
                    'media': media,

                    'error message ': 'please uplnoad proper image format',
                }
                return render(request, 'page/index.html', context)
            else:
                core.pro = media.data_file

            media.save()
            return render(request, 'page/detail.html', {'media': media})

    return render(request, 'page/index.html')


def details(request):
    if not request.user.is_authenticated():
        return render(request, 'page/login.html')
    else:
        user = request.user
        file = core.file
        return render(request, 'detail.html', {'file': file, 'user': user})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'page/index.html')
            else:
                return render(request, 'page/login.html', {'error message': 'Your account has been disabled'})
        else:
            return render(request, 'page/login.html', {'error message': 'Invalid account'})
    return render(request, 'page/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'page/index.html')

    return


def logout(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'page/login.html', context)
