from django.shortcuts import render

def home(request):
    return render(request, 'base/home.html')

def room(request, pk):
    return render(request, 'base/room.html')