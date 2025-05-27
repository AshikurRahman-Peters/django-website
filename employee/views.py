from django.shortcuts import render
from django.http import HttpResponse


def employee(request):
    return HttpResponse("Employee Profile Page")



def profile(request):
    return render(request, 'employee/profile.html')

