from django.urls import path
from . import views

app_name = 'darkChoco'

urlpatterns = [
    path('post/', views.post, name='post'),
    path('jsPost/', views.JsCreatePostView.as_view(), name='jsPost'),
]
