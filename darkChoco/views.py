from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from .models import Letter
from whiteChoco.models import Profile
from django.views import View
from django.http import JsonResponse
import json

def index(request):
    return render(request, 'index.html')

def post(request):
    try :
        profileModel = Profile.objects.get(nickname=request.POST['to_user'])
        if str(profileModel.nickname) == str(request.user.profile) :
            messages.info(request, '나에게는 보낼 수 없습니다!!')
            return redirect('index')
        else :
            letter = Letter()
            letter.user_check = profileModel.user
            letter.to_user = profileModel.nickname
            letter.from_user = request.user.profile
            letter.letter_text = request.POST['letter_text']
            letter.send_date = timezone.datetime.now()
            letter.save()
            messages.info(request, '전송완료!')
            return redirect('index')
    except :
        messages.info(request, '아이디 없음!')
        return redirect('index')

############### JSON ###############
class JsCreatePostView(View):
    def get(self, request):
        response = {}
        response["result"] = "false"
        response["status_code"] = "210"
        response["message"] = "잘못된 요청입니다."
        response["return_url"] = "/"
        return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})

    def post(self, request):
        response = {}
        
        body = request.body.decode('utf8')
        data = json.loads(body)

        try :
            profileModel = Profile.objects.get(nickname=data['to_user'])
            if str(profileModel.nickname) == str(request.user.profile):
                response["result"] = "false"
                response["status_code"] = "211"
                response["message"] = "나에게는 보낼 수 없습니다!!"
                response["return_url"] = "/"
                return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})
            else :
                letter = Letter()
                letter.user_check = profileModel.user
                letter.to_user = profileModel.nickname
                letter.from_user = request.user.profile
                letter.letter_text = data['letter_text']
                letter.send_date = timezone.datetime.now()
                letter.save()
                response["result"] = "false"
                response["status_code"] = "212"
                response["message"] = "전송완료!"
                response["return_url"] = "/"
                return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})
        except :
            response["result"] = "false"
            response["status_code"] = "212"
            response["message"] = "아이디 없음!"
            response["return_url"] = "/"
            return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})











        if User.objects.filter(username=data['username']): 
            response["result"] = "false"
            response["status_code"] = "201"
            response["message"] = "이미 사용중인 아이디 입니다."
            response["return_url"] = "/"
            return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})
        else:
            if data['password1'] == data['password1']: # 비밀번호 1과 2 비교
                try:
                    if Profile.objects.filter(nickname=data['nickname']):
                        response["result"] = "false"
                        response["status_code"] = "202"
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
                    response["status_code"] = "203"
                    response["message"] = "회원가입에 실패하였습니다."
                    response["return_url"] = "/"
            else :
                response["result"] = "false"
                response["status_code"] = "204"
                response["message"] = "비밀번호가 서로 다릅니다."
                response["return_url"] = "/"
            return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})