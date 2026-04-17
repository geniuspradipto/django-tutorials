from django.shortcuts import render, HttpResponse, redirect

from app.models import Student
# Create your views here.
# we will write functions here in this python file and then we will use it as a module

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        mob = request.POST.get('mob')

        student = Student(name=name, roll=roll, mob=mob)
        student.save()

    return render(request, 'home.html')
   

def about(request):
    students = Student.objects.all()
    return render(request, 'about.html', {'students': students})

def contact(request):
    return HttpResponse("Contact Us Page")

def discard(request, roll):
    student = Student.objects.get(roll=roll)
    student.delete()
    return redirect('/about')

def edit(request, roll):
    student = Student.objects.get(roll=roll)
    return render(request, 'edit.html', {'student':student}) # we are passing the value using context dictionary

def update(request, roll):
    student = Student.objects.get(roll=roll)
    student.name = request.POST.get('name')
    student.roll = request.POST.get('roll')
    student.mob = request.POST.get('mob')
    student.save() # this value will be saved with the new info
    return redirect('/about') # the values are stored in the about page