from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from .models import Letter

def index(request):
    try :

        letters = Letter.objects.filter(to_user=request.user).order_by('-send_date')
        context = {
            'letters' : letters
        }
        return render(request, 'index.html', context)
    except :  # 에러 종류
        return render(request, 'index.html')

def post(request):
    try :
        username = User.objects.get(username=request.GET['to_user'])
        letter = Letter()
        letter.to_user = username
        letter.from_user = request.user.get_username()
        letter.letter_text = request.GET['letter_text']
        letter.send_date = timezone.datetime.now()
        letter.save()
        messages.info(request, '전송완료!')
        return redirect('index')
    except :  # 에러 종류
        messages.info(request, '아이디 없음!')
        return redirect('index')