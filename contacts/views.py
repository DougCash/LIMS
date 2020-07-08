from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import ContactForm
from .models import Contacts
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    template_name = 'contacts/index.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return Contacts.objects.all()

class ContactDetailView(DetailView):
    model = Contacts
    template_name = 'contacts/contact-detail.html'

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ContactForm()
    return render(request,'contacts/create.html',{'form': form})

def edit(request, pk, template_name='contacts/edit.html'):
    contact = get_object_or_404(Contacts, pk=pk)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='contacts/confirm_delete.html'):
    contact = get_object_or_404(Contacts, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object':contact})