from django.shortcuts import render
from django.http import HttpResponse
from instructors.models import Instructor
# Create your views here.

def hello(request):
    return render(request, "index.html")
def hellopython(request):
    return render(request, "python.html")
def hellohttp(request):
    print (request.POST)
    return render(request, "http.html")
def instructors_list(request):
    instructors = Instructor.objects.all()
    return render(request, "instructors.html", {"instructors_list": instructors})
