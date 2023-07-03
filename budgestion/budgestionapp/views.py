from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def inscription(request):
    return render(request, 'inscription.html')

def dashboard(request):
    return render(request, 'dashboard.html')


def dashboardadmin(request):
    return render(request, 'dashboard-admin.html')