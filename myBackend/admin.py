from django.contrib import admin
from .models import ClientDetails,Appointment,Employee,EmployeeFreeSlot,Services,AppointmentTicket

admin.site.register(ClientDetails)
admin.site.register(Appointment)
admin.site.register(Employee)
admin.site.register(EmployeeFreeSlot)
admin.site.register(Services)
admin.site.register(AppointmentTicket)
