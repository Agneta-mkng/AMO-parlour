from rest_framework import serializers
from.models import Service,Appointment,EmployeeFreeSlot

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields=["service_name","service_price"]

class ApointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields=["appointment_date","client_email","appointment_time","service"]
        #This will be used to get data from the user

class EmployeeFreeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeFreeSlot
        fields=["free-day","free_time"]


