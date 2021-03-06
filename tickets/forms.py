from django.forms import ModelForm
from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'client', 'requested_by', 'type', 'description', 'assigned', 'labels']