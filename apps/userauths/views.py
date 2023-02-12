from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from apps.userauths.forms import UserRegisterForm


def register_view(request):
    if request.method =='POST':
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
