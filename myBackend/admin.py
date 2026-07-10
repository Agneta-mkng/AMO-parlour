from django.contrib import admin
from .models import ClientDetails,Appointment,Employee,EmployeeFreeSlot,Service,AppointmentTicket

admin.site.register(ClientDetails)
admin.site.register(Appointment)
admin.site.register(Employee)
admin.site.register(EmployeeFreeSlot)
admin.site.register(Service)
admin.site.register(AppointmentTicket)
