from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegisterForm
from website.models import Article




def login_view(request):
    next = request.GET.get('next')
    title = "Login"
    emo_recog_article = Article.objects.get(title__startswith="Emotion")
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    return render(request, "accounts/login_form.html", {'form': form, 'title': title, 'emo_recog_article': emo_recog_article})


def register_view(request):
    title = "Register"
    emo_recog_article = Article.objects.get(title__startswith="Emotion")
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect('/')
    context = {
        'form': form,
        'title': title,
        'emo_recog_article': emo_recog_article
    }
    return render(request, "accounts/login_form.html", context=context)


def logut_view(request):
    logout(request)
    return redirect('/')
