from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import ContactForm, LocationForm
from .models import Contacts, Locations
from django.views.generic import ListView, DetailView

class ContactIndexView(ListView):
    template_name = 'contacts/index.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return Contacts.objects.all()

class ContactDetailView(DetailView):
    model = Contacts
    template_name = 'contacts/contact-detail.html'

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_index')
    form = ContactForm()
    return render(request,'contacts/create.html',{'form': form})

def contact_edit(request, pk, template_name='contacts/edit.html'):
    contact = get_object_or_404(Contacts, pk=pk)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact_index')
    return render(request, template_name, {'form':form})

def contact_delete(request, pk, template_name='contacts/confirm_delete.html'):
    contact = get_object_or_404(Contacts, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('contact_index')
    return render(request, template_name, {'object':contact})


class LocationIndexView(ListView):
    template_name = 'locations/index.html'
    context_object_name = 'location_list'

    def get_queryset(self):
        return Locations.objects.all()


class LocationDetailView(DetailView):
    model = Locations
    template_name = 'locations/location-detail.html'


def location_create(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_index')
    form = LocationForm()
    return render(request,'locations/create.html',{'form': form})

def location_edit(request, pk, template_name='locations/edit.html'):
    contact = get_object_or_404(Locations, pk=pk)
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('location_index')
    return render(request, template_name, {'form':form})

def location_delete(request, pk, template_name='locations/confirm_delete.html'):
    contact = get_object_or_404(Locations, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('location_index')
    return render(request, template_name, {'object':contact})