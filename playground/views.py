from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request -> response
#request handler
#action
def say_hello(request):
    # usually with request we can pull data from data base
    #trensform
    #send emails etc
   return HttpResponse('hello world')
