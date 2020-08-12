from django.shortcuts import render
from student.models import Student

# Create your views here.

def viewmark(request):
    print("----------------")
    return render(request, "addmark.html", {})

def addMark(request):
    rollno = int(request.POST['rollno'])
    name = request.POST['name']
    totalmark = int(request.POST['totalmark'])
    student = Student()
    student.rollno = rollno
    student.name = name
    student.toltalmark = totalmark
    Student.save(student)
    return render(request, "addmark.html", {"result":"SUCCESS"})


