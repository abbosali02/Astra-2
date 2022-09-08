from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.aboutPage, name='about'),
    path('team/', views.teamPage, name='team'),
    path('result/', views.resultPage, name='result'),
    path('contact/', views.contact, name='contact'),
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
    path('apply/', views.apply, name='apply' ),
    path('team/<slug:slug>/', views.team, name='team_detail_url'),
    path('teacherfirst/<slug:slug>/', views.firstTeacher, name='first_detail_url'),
    path('teachersecond/<slug:slug>/', views.secondTeacher, name='second_detail_url'),
    path('programs/', views.programs, name='programs'),
    path('priceFirst/', views.priceFirst, name='priceFirst'),
    path('exam/', views.Exam, name="exam")
  
    
    
]
