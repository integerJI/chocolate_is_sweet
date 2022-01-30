from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from .models import Letter
from whiteChoco.models import Profile

def index(request):
    return render(request, 'index.html')

def post(request):
    try :
        profileModel = Profile.objects.get(nickname=request.GET['to_user'])
        if str(profileModel.nickname) == str(request.user.profile) :
            messages.info(request, '나에게는 보낼 수 없습니다!!')
            return redirect('index')
        else :
            letter = Letter()
            letter.user_check = profileModel.user
            letter.to_user = profileModel.nickname
            letter.from_user = request.user.profile
            letter.letter_text = request.GET['letter_text']
            letter.send_date = timezone.datetime.now()
            letter.save()
            messages.info(request, '전송완료!')
            return redirect('index')
    except :
        messages.info(request, '아이디 없음!')
        return redirect('index')