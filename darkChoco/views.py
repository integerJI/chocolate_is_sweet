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
        response["error_code"] = "301"
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
                response["error_code"] = "302"
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
                response["error_code"] = "303"
                response["message"] = "전송완료!"
                response["return_url"] = "/"
                return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})
        except :
            response["result"] = "false"
            response["error_code"] = "304"
            response["message"] = "아이디 없음!"
            response["return_url"] = "/"
            return JsonResponse(response, json_dumps_params = {'ensure_ascii': False})