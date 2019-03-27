from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import User

class Form1(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    if request.method=="POST":
        f = request.POST["username"]
        print (f)
        return HttpResponse(f+"login Success!!!")
    else:
        context = {'':'' }
        return render(request, 'login.html', context)

def login(request):
    if request.method=="POST":
        username = request.POST["username"]
        passwd = request.POST["password"]
        _user_password = User.objects.get(name=username)
        if username == _user_password.name and passwd == _user_password.password:
            return  render(request, 'index.html')
    else:
        return HttpResponse( "login Fail!!!")

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)