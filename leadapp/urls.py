from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewLeads, name="viewLeads"),
    path('add/', views.addLead, name="addLead"),
    path('update/<int:pk>/', views.updateLead, name="updateLead"),
    path('delete/<int:pk>/', views.removeLead, name="removeLead"),
    
    path('<int:pk>/contact', views.viewContact,  name="viewContact"),
    path('<int:pk>/contact/all', views.getAllContacts, name= "allContacts"),
    path('<int:pk>/contact/add', views.addContact, name="addContact"),
    

]
