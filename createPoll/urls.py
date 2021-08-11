from django.urls import path
from . import views

app_name = 'createPoll'

urlpatterns = [
    path('',views.createPoll,name="createPoll"),
]