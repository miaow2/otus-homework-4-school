from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, HttpResponseRedirect, redirect, render
from django.urls import reverse
from django.views.generic.base import View
from rest_framework.authtoken.models import Token

from .forms import RegisterForm


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = AuthenticationForm(request)

        if request.user.is_authenticated:
            return redirect('home')

        return render(request, self.template_name, {
            'form': form,
        })

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            login(request, form.get_user())

            return redirect('home')

        return render(request, self.template_name, {
            'form': form,
        })


class LogoutView(View):

    def get(self, request):

        logout(request)

        response = HttpResponseRedirect(reverse('home'))
        response.delete_cookie('session_key')

        return response


class ProfileView(LoginRequiredMixin, View):
    template_name = 'users/profile.html'

    def get(self, request):

        return render(request, self.template_name, {})



class RegisterView(View):
    template_name = 'register.html'
    form = RegisterForm

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('login')
        else:
            return render(request, self.template_name, {"form": form})


class TokenCreateView(LoginRequiredMixin, View):

    def get(self, request):

        try:
            token = Token.objects.get(user=request.user)
            token.delete()
        except Token.DoesNotExist:
            pass
        Token.objects.create(user=request.user)

        return redirect('users:profile')