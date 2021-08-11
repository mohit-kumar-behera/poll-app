from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home,name="home"),
    path('vote/',views.vote,name="vote"),
    path('result/',views.result,name="result")
]