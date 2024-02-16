from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Persons


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    abc = Persons.objects.all()
    return render(request, "index.html", {'result': obj,'res': abc})

# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("HA------------
#     I I AM CONTACT VIEW")
