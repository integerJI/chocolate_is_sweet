from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth
from django.views import View
from whiteChoco.models import Profile
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

class CreateUserView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                    username=request.POST["username"],
                    email=request.POST["username"],
                    password=request.POST["password1"]
                )
            nickname = request.POST["nickname"]
            profile = Profile(user=user, nickname=nickname)
            profile.save()
            auth.login(request,user)
            return redirect('index')

class Loginviews(LoginView):
    template_name = settings.LOGIN_URL
login = Loginviews.as_view()

class LogoutViews(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL
logout = LogoutViews.as_view()
