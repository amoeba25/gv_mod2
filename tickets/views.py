from django.shortcuts import redirect, render
from .models import Ticket
from .forms import TicketForm


# Create your views here.
def viewTicket(request):
    tickets = Ticket.objects.all()
    context = {"tickets": tickets}
    return render(request, "tickets/ticketHome.html", context)

# creation
def addTicket(request):
    
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewTickets")
    else:
        form = TicketForm()
        context = {"form": form}
    return render(request, "tickets/ticketsAdd.html", context)

# update
def updateTicket(request, pk):
    
    update_obj = Ticket.objects.get(id= pk)
    form = TicketForm(instance=update_obj)
    
    if request.method == "POST":
        form = TicketForm(instance=update_obj, data= request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewTickets")
    
    context ={"form": form}
    return render(request, "tickets/ticketUpdate.html", context)    
    
# deletion
def removeTicket(request, pk):
    delete_obj = Ticket.objects.get(id= pk)
    delete_obj.delete()
    return redirect("viewTickets")

# ticket status 
def changeTicketStatus(request, pk):
    status_filter = Ticket.objects.get(id = pk)
    print(status_filter)
    if(status_filter.status == "Open"):
        Ticket.objects.filter(id = pk).update(status ="Closed")
    else:
        Ticket.objects.filter(id = pk).update(status ="Open")
    return redirect("viewTickets")

# assignment change
def changeAssignment(request, pk):
    Ticket.objects.filter(id = pk).update(assigned = request.user.username)
    return redirect("viewTickets")