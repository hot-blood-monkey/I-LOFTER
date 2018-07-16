from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm, RegisterForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            # 使用


            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('认证成功')
                else:
                    return HttpResponse('该用户没有权限')

    else:
        """当是被一个get请求时，实例化一个登录表单，交给template渲染"""
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            return render(request, 'account/register_done.html',
                          {'new_user':new_user})

    else:
        form = RegisterForm()

    return render(request, 'account/register.html',
                  {'form':form})

