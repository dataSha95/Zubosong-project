from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def programs(request):
    return render(request, 'home/programs.html')

def community(request):
    return render(request, 'home/community.html')

def get_involved(request):
    return render(request, 'home/get_involved.html')

def contact(request):
    return render(request, 'home/contact.html')
