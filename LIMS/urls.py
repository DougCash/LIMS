"""LIMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from contacts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', views.ContactIndexView.as_view(), name='contact_index'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),
    path('contacts/edit/<int:pk>/', views.contact_edit, name='contact_edit'),
    path('contacts/create/', views.contact_create, name='contact_create'),
    path('contacts/delete/<int:pk>/', views.contact_delete, name='contact_delete'),
    path('locations/', views.LocationIndexView.as_view(), name='location_index'),
    path('locations/<int:pk>/', views.LocationDetailView.as_view(), name='location_detail'),
    path('locations/edit/<int:pk>/', views.location_edit, name='location_edit'),
    path('locations/create/', views.location_create, name='location_create'),
    path('locations/delete/<int:pk>/', views.location_delete, name='location_delete'),
]
