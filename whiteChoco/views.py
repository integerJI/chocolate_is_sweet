from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import auth, messages
from django.views import View
from whiteChoco.models import Profile
from darkChoco.models import Letter
from django.http import JsonResponse
import json

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
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            profileModel = Profile.objects.get(user=user)
            return redirect('whiteChoco:userpage', nickname=profileModel.nickname)
        else:
            messages.info(request, '아이디, 패스워드를 확인하세요')
            return redirect('index')

class LogoutViews(LogoutView):
    next_page = 'index'
logout = LogoutViews.as_view()

def userpage(request, nickname):
    try:
        profileModel = Profile.objects.get(nickname=nickname)
        letters = Letter.objects.filter(to_user=nickname).order_by('-send_date')
        context = {
            'nickname' : profileModel.nickname,
            'letters' : letters,
        }
        return render(request, 'userpage.html', context=context)
    except:
        messages.info(request, '사용자 없음!')
        return redirect('index')

############### JSON ###############
class JsCreateUserView(View):
    def get(self, request):
        return render(request, 'singup.html')

    def post(self, request):
        response = {}
        
        body = request.body.decode('utf8')
        data = json.loads(body)

        if User.objects.filter(username=data['username']): 
            response["result"] = "false"
            response["error_code"] = "201"
            response["message"] = "이미 사용중인 아이디 입니다."
            response["return_url"] = "/"
            return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})
        else:
            if data['password1'] == data['password1']: # 비밀번호 1과 2 비교
                try:
                    if Profile.objects.filter(nickname=data['nickname']):
                        response["result"] = "false"
                        response["error_code"] = "202"
                        response["message"] = "이미 사용중인 닉네임 입니다."
                        response["return_url"] = "/"
                        return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})
                    else:
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
                except KeyError:
                    response["result"] = "false"
                    response["error_code"] = "203"
                    response["message"] = "회원가입에 실패하였습니다."
                    response["return_url"] = "/"
            else :
                response["result"] = "false"
                response["error_code"] = "204"
                response["message"] = "비밀번호가 서로 다릅니다."
                response["return_url"] = "/"
            return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})