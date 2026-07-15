from django.db import models


class Services(models.Model):
    service_name=models.CharField(max_length=100)
    service_price=models.IntegerField()
    service_des=models.CharField(max_length=200)

class ClientDetails(models.Model):
    client_email=models.EmailField(max_length=150,unique=True)
    client_name=models.CharField(max_length=100,blank=False)
    client_contact=models.IntegerField(blank=False)
    client_password=models.CharField(max_length=150)

class Appointment(models.Model):
    appointment_id=models.AutoField(primary_key=True,blank=False)
    appointment_date=models.DateField()
    client_email=models.ForeignKey(ClientDetails,on_delete=models.PROTECT)
    appointment_time=models.DateTimeField()
    service=models.ForeignKey(Services,on_delete=models.PROTECT)

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
