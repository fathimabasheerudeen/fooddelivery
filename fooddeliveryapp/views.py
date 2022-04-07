from django.http import HttpResponse
from django.shortcuts import render
from . models import Food

# Create your views here.
def demo(request):
    obj=Food.objects.all()
    return render(request, "index.html",{'result':obj})