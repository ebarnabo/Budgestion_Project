"""
URL configuration for budgestion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from budgestionapp import views

urlpatterns = [
    path('', views.connexion, name='connexion'),
    path('logout/', views.logout, name='logout'),
    path('inscription/', views.inscription, name='inscription'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard-admin/', views.dashboardadmin, name='dashboardadmin'),
    path('admin/', admin.site.urls, name='admin'),
    path('addLigne/', views.addLigne, name='addLigne'),
    path('delLigne/', views.delLigne, name='delLigne'),
    path('delLigneAdmin/', views.delLigneAdmin, name='delLigneAdmin'),
    path('addUser/', views.addUser, name='addUser'),
    path('delUser/', views.delUser, name='delUser'),
    path('profile/', views.profile, name='profile'),
    path('editEtudiant/', views.editEtudiant, name='editEtudiant'),
    path('editEtudiantPasse/', views.editEtudiantPasse, name='editEtudiantPasse'),
    
]
