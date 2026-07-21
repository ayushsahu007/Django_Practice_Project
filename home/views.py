from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples = [
        {"name" : "Ayush Sahu","age":20},
        {"name" : "Rorona Zoro","age":25},
        {"name" : "Black foot","age":23},
        {"name" : "Tony Choper","age":15},
        {"name" : "Sea son Jimbe","age":50}
    ]
    
    vegetables = ['Pumpkin','Tomato','Patato']
    
    return render(request , "index.html", context={'peoples' : peoples,'vegetables' : vegetables})

def about(request):
    context = {'page' : 'About'}
    return render(request , "about.html")

def contact(request):
    context = {'page' : 'Contact'}
    return render(request , "contact.html")

def success_page(request):
    context = {'page' : 'contact'}
    return HttpResponse("<h1>Hey this is Success Page<h1>")