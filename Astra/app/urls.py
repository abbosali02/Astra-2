from django.urls import path
from . import views

urlpatterns = [
    
    path('seven/<slug:slug>/', views.seven, name='seven_detail_url'),
    path('sevenhalf/<slug:slug>/', views.sevenhalf, name='sevenhalf_detail_url'),
    path('eight/<slug:slug>/', views.eight, name='eight_detail_url'), 
    path('eighthalf/<slug:slug>/', views.eighthalf, name='eighthalf_detail_url' ),
    path('policy/', views.policy, name='policy'),
    path('thank/', views.thank, name='thank'),
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('third/', views.third, name='third'),
    path('fourth/', views.fourth, name='fourth'),

    path('team/<slug:slug>/', views.team, name='team_detail_url'),
    path('teacherfirst/<slug:slug>/', views.firstTeacher, name='first_detail_url'),
    path('teachersecond/<slug:slug>/', views.secondTeacher, name='second_detail_url'),
    path('teacherthird/<slug:slug>/', views.thirdTeacher, name='third_detail_url'),
    path('teacherhead/<slug:slug>/', views.Head, name='head_detail_url'),
    path('teachermain/<slug:slug>/', views.Main, name='main_detail_url'),
    path('priceFirst/', views.priceFirst, name='priceFirst'),
    path('exam/', views.Exam, name="exam"),
    path('', views.homepage, name='homepage'),
    path('index/', views.index, name='index')
  
    
    
]
