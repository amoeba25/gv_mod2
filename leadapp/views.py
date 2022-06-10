from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Leads, Contact
from .forms import LeadForm, ContactForm
from django.core import serializers


# Create your views here.
def viewLeads(request):
    
    model = Leads.objects.all()
    context = {"leads": model}
    return render(request, "leadapp/leadHome.html", context)

# creation
def addLead(request):
    
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewLeads")
    else:
        form = LeadForm()
        context = {"form": form}
    return render(request, "leadapp/leadAdd.html", context)

# update
def updateLead(request, pk):
    
    update_obj = Leads.objects.get(id= pk)
    form = LeadForm(instance=update_obj)
    
    if request.method == "POST":
        form = LeadForm(instance=update_obj, data= request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewLeads")
    
    context ={"form": form}
    return render(request, "leadapp/leadUpdate.html", context)    
    
# deletion
def removeLead(request, pk):
    
    delete_obj = Leads.objects.get(id= pk)
    delete_obj.delete()
    return redirect("viewLeads")


# contact view 
def viewContact(request, pk):
    contactForm = ContactForm()
    context = {"contactForm": contactForm}
    return render(request, "leadapp/sub/contactHome.html", context)

# get all contacts
def getAllContacts(request,pk):
    contacts = Contact.objects.all()
    data = serializers.serialize("json", contacts)
    return JsonResponse(data,safe= False)
    
# creation
def addContact(request, pk):
    
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contact = contactform.save()
            return JsonResponse(model_to_dict(contact), safe= False)
    
