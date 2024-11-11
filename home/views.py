from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def programs(request):
    return render(request, 'home/programs.html')


def community(request):
    return render(request, 'home/community.html') 