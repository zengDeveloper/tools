from django.shortcuts import render
from . import imageService
from django.http import HttpResponse
def hello(request):
    return render(request,'index.html')

def imageHandler(request): 
	return  HttpResponse(imageService.ocrImage(request))