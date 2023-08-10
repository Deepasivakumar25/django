from django.shortcuts import render
from django.http import HttpResponse
from .student_form import StudentForm

def get_index(request):
    return render(request,"index.html",{})

def get_layout(request):
    return render(request,"layout.html",{})

def main_layout(request):
    return render(request,"main.html",{"key":"heading"})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # Handle successful form submission
    else:
        form = StudentForm()
    
    return render(request, 'create_student.html', {'form': form})


