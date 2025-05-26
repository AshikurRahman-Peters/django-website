from django.http import HttpResponse


def employee(request):
    return HttpResponse("This is the employee page.");



def profile(request):
    return HttpResponse("This is the profile page.");

