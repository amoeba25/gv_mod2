from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewTicket, name="viewTickets"),
    path('add/', views.addTicket, name="addTickets"),
    path('update/<int:pk>/', views.updateTicket, name="updateTickets"),
    path('delete/<int:pk>/', views.removeTicket, name="removeTickets"),
    path('status/<int:pk>', views.changeTicketStatus, name="statusTicket"),
    path('assignment/<int:pk>', views.changeAssignment, name="assignTicket")

]
