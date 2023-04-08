from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "home/index.html")

def login(request):
    return render(request, "login/login.html")

def list(request):
    return HttpResponse("menu/Login.html")
    
def post(request):
    return HttpResponse("post")
    
def help(request):
    return render(request, "help/index.html")