from socket import ALG_SET_AEAD_ASSOCLEN
from django.shortcuts import render, redirect
from django.views import generic

from leads.forms import LeadModelForm
from .models import *
from agents.models import *
from .forms import *

class DashboardView(generic.ListView):
    template_name = 'leads/dashboard.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

def dashboard(request):
    leads = Lead.objects.all()
    return render(request, "leads/dashboard.html", {'leads': leads})

def lead_details(request, slug):
    lead = Lead.objects.get(id=slug)
    agents = Agent.objects.all()
    return render(request, "leads/lead_details.html", {'lead': lead, 'agents': agents})


class CreateView(generic.CreateView):
    template_name = "leads/create_lead.html"
    context_object_name = 'agents'

def create_lead(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        agent = request.POST['agent']
        print(agent)
        agent_found = Agent.objects.get(agent__id=int(agent))

        if agent_found is not None:
            Lead.objects.create(firstname=firstname, lastname=lastname, age=age, agent=agent_found)
            # lead.save()
            return redirect("leads:dashboard")
        
    agents = Agent.objects.all()
    return render(request, "leads/create_lead.html", {'agents': agents})


def create_form(request):
    form = LeadModelForm()

    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads:dashboard')

    context = {'form': form}
    return render(request, 'leads/create_form.html', context)

def delete_lead(request):
    if request.method == "POST":
        id = request.POST["id"]
        Lead.objects.get(id=id).delete()
    
    return redirect("leads:dashboard")

def edit_lead(request, id):
    lead = Lead.objects.get(id=id)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        lead_updated = LeadModelForm(request.POST, instance=lead)
        if lead_updated.is_valid():
            lead_updated.save()
            return redirect('leads:dashboard')
    
    context = {
        'form': form
    }
    return render(request, "leads/edit_lead.html", context)

# def create_form(request):
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             # form_data = form.cleaned_data

#             firstname = form.cleaned_data['firstname']
#             lastname = form.cleaned_data['lastname']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()

#             Lead.objects.create(firstname=firstname, lastname=lastname, age=age, agent=agent)
#             return redirect("leads:dashboard")
    
#     context = {'form': form}
#     return render(request, "leads/create_form.html", context)