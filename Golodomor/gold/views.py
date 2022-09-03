from django.shortcuts import render
def index(request):
    return render(request, "home.html")
def about(request):
    return rrende(request, "about.html")

