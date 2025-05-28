from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    text = {
        "name": "John Doe",
        "age": 30,  
        "phone": "123-456-7890",
        "email": "asbc@gmail.com",
        "skills": ["Python", "Django", "JavaScript", "HTML", "CSS"],
        "projects": [
            {
                "title": "Portfolio Website",
                "description": "A personal portfolio website to showcase my projects and skills.",
                "link": "abc",
    }
        ]
    }


    return render(request, 'index.html', text)


def portfolio(request):
    return render(request, 'portfolio.html')


def service(request):
    return render(request, 'service.html')

