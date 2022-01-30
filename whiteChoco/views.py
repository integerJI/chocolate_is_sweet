from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import auth, messages
from django.views import View
from whiteChoco.models import Profile
from darkChoco.models import Letter

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

class LoginUserView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = User.objects.get(username=request.POST["username"])
        profileModel = Profile.objects.get(user=user)
        login(request, user)
        return redirect('whiteChoco:userpage', nickname=profileModel.nickname)

class LogoutViews(LogoutView):
    next_page = 'index'
logout = LogoutViews.as_view()

def userpage(request, nickname):
    try :
        profileModel = Profile.objects.get(nickname=nickname)
        letters = Letter.objects.filter(to_user=request.user.profile).order_by('-send_date')
        context = {
            'nickname' : profileModel.nickname,
            'letters' : letters,
        }
        return render(request, 'userpage.html', context=context)
    except :
        messages.info(request, '사용자 없음!')
        return redirect('index')