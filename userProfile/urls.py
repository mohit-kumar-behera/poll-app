from django.urls import path
from . import views

app_name = 'userProfile'

urlpatterns = [
    path('u/',views.userProfile,name="userProfile"),
    path('v/<str:user>',views.viewProfile,name="viewProfile"),
    path('logout/',views.logout,name="logout")
]