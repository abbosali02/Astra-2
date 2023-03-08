from wsgiref.util import request_uri
from django import http
from django.shortcuts import render
from .models import *

# Create your views here.


def homepage(request):
     results = Results.objects.all()
     team = Team.objects.all()
     firstT = FirstTeacher.objects.all()
     first = FirstTeacher.objects.all()
     second = SecondTeacher.objects.all()
     third = ThirdTeacher.objects.all()
     main = MainTeacher.objects.all()
     head = HeadTeacher.objects.all()

     if request.method == "POST":
        contact = contactMe()
        name = request.POST.get('name')
        last = request.POST.get('last')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        telegram = request.POST.get('telegram')

        contact.name = name
        contact.last = last
        contact.age = age
        contact.phone = phone
        contact.email = email
        contact.telegram = telegram
        contact.save()
        return render(request, 'main/thank.html')
     return render(request, 'main/index.html', {
          'results': results,
          'team':team, 
          'firstT':firstT,
          'first':first,
          'second':second,
          'third' : third,
          'main':main,
          'head':head
          })

def index(request):
     results = Results.objects.all()
     team = Team.objects.all()
     firstT = FirstTeacher.objects.all()
     first = FirstTeacher.objects.all()
     second = SecondTeacher.objects.all()

     if request.method == "POST":
        contact = contactMe()
        name = request.POST.get('name')
        last = request.POST.get('last')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        telegram = request.POST.get('telegram')

        contact.name = name
        contact.last = last
        contact.age = age
        contact.phone = phone
        contact.email = email
        contact.telegram = telegram
        contact.save()
        return render(request, 'main/thank.html')
     return render(request, 'main/index.html', {
          'results': results,
          'team':team, 
          'firstT':firstT,
          'first':first,
          'second':second,
          })






def seven(request, slug):
     seven = Seven.objects.get(slug__iexact=slug)
     return render(request, 'main/overview/seven.html', {'seven':seven})
def sevenhalf(request, slug):
     sevenhalf = SevenHalf.objects.get(slug__iexact=slug)
     return render(request, 'main/overview/sevenhalf.html', {'sevenhalf':sevenhalf})
def eight(request, slug ):
     eight = Eight.objects.get(slug__iexact=slug)
     return render(request, 'main/overview/eight.html', {'eight':eight})
def eighthalf(request, slug):
     eighthalf = EightHalf.objects.get(slug__iexact=slug)
     return render(request, 'main/overview/eighthalf.html', {'eighthalf':eighthalf})
def policy(request):
     return render(request, 'main/policy.html')

def thank(request):
     return render(request, 'main/thank.html')
def first(request):
     seven = Seven.objects.order_by('-id')
     return render(request, 'main/pagination/first.html', {'seven':seven})
def second(request):
     sevenhalf = SevenHalf.objects.order_by('-id')
     return render(request, 'main/pagination/second.html', {'sevenhalf':sevenhalf})
def third(request):
     eight = Eight.objects.order_by('-id')
     return render(request, 'main/pagination/third.html', {'eight':eight})
def fourth(request):
     eighthalf = EightHalf.objects.order_by('-id')
     return render(request, 'main/pagination/fourth.html', {'eighthalf' : eighthalf})

def apply(request):
     if request.method == "POST":
        apply = Apply()
        name = request.POST.get('name')
        residence = request.POST.get('residence')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        education = request.POST.get('education')
        telegram = request.POST.get('telegram')
        university = request.POST.get('university')
        ielts = request.POST.get('ielts')
        other = request.POST.get('other')
        job1 = request.POST.get('job1')
        job2 = request.POST.get('job2')
        languages = request.POST.get('languages')

        apply.name = name
        apply.residence = residence
        apply.age = age
        apply.phone = phone
        apply.education = education
        apply.telegram = telegram
        apply.university = university
        apply.ielts = ielts
        apply.other = other
        apply.job1 = job1
        apply.job2 = job2
        apply.languages = languages
        
        apply.save()
        return render(request, 'main/thank.html')
     return render(request, 'main/apply.html')
def team(request, slug):
     team = Team.objects.get(slug__iexact=slug)
     return render(request, 'main/team/team.html', {'team':team} )

def firstTeacher(request, slug):
     first = FirstTeacher.objects.get(slug__iexact=slug)
     return render(request, 'main/team/first.html', {'first':first})
def secondTeacher(request, slug):
     second = SecondTeacher.objects.get(slug__iexact=slug)
     return render(request, 'main/team/second.html', {'second':second})
def thirdTeacher(request, slug):
     third = ThirdTeacher.objects.get(slug__iexact = slug)
     return render(request, 'main/team/third.html', {'third': third} )



def priceFirst(request):
     return render(request, 'main/programs/programs.html')
def Exam(request):
     return render(request, 'main/exam.html')

def Main(request,slug):
     main = MainTeacher.objects.get(slug__iexact = slug)
     return render(request, 'main/team/main.html', {'main':main})
def Head(request, slug):
     head = HeadTeacher.objects.get(slug__iexact = slug)
     return render(request, 'main/team/head.html', {'head':head})

       