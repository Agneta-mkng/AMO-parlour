from django.db import models
from django.core.validators import MinLengthValidator

class Service(models.Model):
    service_name=models.CharField(max_length=100)
    service_price=models.IntegerField()

class ClientDetails(models.Model):
    client_email=models.CharField(max_length=150)
    client_name=models.CharField(max_length=100,blank=False)
    client_contact=models.IntegerField(blank=False)
    #learn more on how to enforce length restrictions for a phone number using regex validator
    client_password=models.CharField(max_length=50,validators=[MinLengthValidator(12,"Password length should be at least 12 ccharacters")])

class Appointment(models.Model):
    appointment_id=models.AutoField(primary_key=True,blank=False)
    appointment_date=models.DateField()
    client_email=models.ForeignKey(ClientDetails,on_delete=models.PROTECT)
    appointment_time=models.DateTimeField()
    service=models.ForeignKey(Service,on_delete=models.PROTECT)

class Employee(models.Model):
    emp_id=models.CharField(max_length=50)
    emp_name=models.CharField(max_length=100)
    job_description=models.CharField(max_length=100)

class EmployeeFreeSlot(models.Model):
    emp_id=models.ForeignKey(Employee,on_delete=models.PROTECT)
    free_day=models.DateField()
    free_time=models.DateTimeField()

class AppointmentTicket(models.Model):
    emp_id=models.ForeignKey(EmployeeFreeSlot,on_delete=models.PROTECT)
    appointment_id=models.ForeignKey(Appointment,on_delete=models.PROTECT)
    opened_at=models.DateTimeField(auto_now_add=True)
    appointment_status=models.CharField(max_length=100)
