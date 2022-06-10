from django.forms import ModelForm
from .models import Leads,Contact

class LeadForm(ModelForm):
    class Meta:
        model = Leads
        fields = "__all__"
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"