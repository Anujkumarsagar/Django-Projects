from django.http import HttpResponse
from django.shortcuts import render

def home(req): 
    # return HttpResponse("hell world , this is a home route")
    return render(req, template_name="website/home.html")

def about(req):
    # return HttpResponse("this is the about route")
    return render(req, template_name="website/about.html")


def contact(req):
    # return HttpResponse("this is the contact route")
    return render(req, template_name="website/contact.html")





# creae functions -> urls.py [1: import , 2 : setup routes based on functions]