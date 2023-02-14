from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from apps.userauths.forms import UserRegisterForm
from apps.userauths.models import User


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Привет {username}, твоя учетка была успешно создана')
            new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('index')
    else:
        form = UserRegisterForm()
        print('Пользователь не может быть зарегистрирован')
    context = {
        'form': form,
    }
    return render(request, 'userauths/sing-up.html', context)


def login_view(request):
    if request.user.is_authenticated:
        messages.success(request,f'Ты уже вошел в систему')
        return redirect("index")
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Ты вошел в систему")
                return redirect('index')
            else:
                messages.warning(request, "Пользователь не сушествует создайте учетную запись")
        except:
            messages.warning(request, f'Пользователь {email} не сушеструет')
    return render(request, 'userauths/sing-in.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Ты вышел из системыю')
    return redirect('sign-in')