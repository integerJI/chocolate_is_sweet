from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth
from django.views import View
from whiteChoco.models import Profile
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login

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
            return redirect('whiteChoco:userpage', nickname=nickname)

# class Loginviews(LoginView):
#     template_name = settings.LOGIN_URL
# login = Loginviews.as_view()

def user_login(request):
    if request.method == "POST":
        user = User.objects.get(username=request.POST["username"])
        profileModel = Profile.objects.get(user=user)
        login(request, user)
        return redirect('whiteChoco:userpage', nickname=profileModel.nickname)
    else :
        return render(request, 'login.html')

class LogoutViews(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL
logout = LogoutViews.as_view()

def userpage(request, nickname):
    try :
        profileModel = Profile.objects.get(nickname=nickname)
        context = {
            # 'username' : userModel.username,
            'nickname' : profileModel.nickname
        }
        return render(request, 'userpage.html', context=context)
    except :
        messages.info(request, '사용자 없음!')
        return render(request, 'err-404.html')
