from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Courses
from ..landr.models import Register
from django.db.models import Count
# Create your views here.
def index(request):
    context = {
    "courses": Courses.objects.all(),
    }
    return render(request, 'courses/courses.html', context)

def add_course(request):
    if request.method=="POST":
        Courses.objects.create(course_name = request.POST["course_name"], description = request.POST["description"])
    return redirect(reverse('courses:index'))

def remove(request, id):
    this_course = Courses.objects.get(id=id)
    context = {
        "course": this_course
    }
    return render(request, 'courses/remove.html', context)

def remove_confirm(request):
    Courses.objects.filter(id=request.POST['course_id']).delete()
    return redirect(reverse('courses:index'))

def keep(request):
    return redirect(reverse('courses:index'))

def users_courses_index(request):
    context = {
    "courses": Courses.objects.all().annotate(number = Count('users')),
    "users": Register.objects.all(),
    }
    return render(request, "courses/users_courses.html", context)

def users_courses_add(request):
    if request.method=="POST":
        course = Courses.objects.get(id = request.POST['courses'])
        user = Register.objects.get(id = request.POST['users'])
        course.users.add(user)
        print(course.users)
    return redirect(reverse('courses:users_courses_index'))
