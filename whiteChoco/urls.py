from django.urls import path
from . import views

app_name = 'whiteChoco'

urlpatterns = [
    path('signup/', views.CreateUserView.as_view(), name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('userpage/<str:nickname>', views.userpage, name='userpage'),
]
