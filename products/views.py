from django.shortcuts import render
from .models import Product

from django.http import HttpResponse

def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products': products})
    #return HttpResponse("<h1>Welcome</h1>")
def about(request):
    return HttpResponse("<h1>About</h1>")
