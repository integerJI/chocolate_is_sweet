from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Letter

def index(request):
    return render(request, 'index.html')

def post(request):
    letter = Letter()
    letter.letter_text = request.GET['post_context']
    letter.send_date = timezone.datetime.now()
    letter.save()
    return redirect('index')
