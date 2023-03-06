from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def anuska(request):
    return HttpResponse('<a href="www.amazon.com">amazon.com')

def kattappa(vennupotu):
    return HttpResponse('<h1 style>banisathvam na bhadyatha</h1>')