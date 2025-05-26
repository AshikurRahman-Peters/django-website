from django.http import HttpResponse


def about(request):
    return HttpResponse("This is the about page.");

def home(request):
    return HttpResponse("This is the home page.");

def contact(request):
    return HttpResponse("This is the contact page.");