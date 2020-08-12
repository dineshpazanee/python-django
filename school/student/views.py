from django.shortcuts import render
from student.models import Student

# Create your views here.


def loadIndex(request):
    return render(request, "index.html")


def getResult(request):
    rollno = request.GET['rollno']
    rollno = int(rollno)
    value = Student.objects.filter(rollno=rollno)
    return render(request, "result.html", {"result":value})
