from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('超贼帅')
def detail(request,num):
    return HttpResponse("detail%s"%num)