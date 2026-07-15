from rest_framework import serializers
from.models import Services,Appointment,EmployeeFreeSlot,ClientDetails

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Services
        fields=["service_name","service_price","service_des"]

class ApointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields=["appointment_date","client_email","appointment_time","service"]
        #This will be used to get data from the user

class EmployeeFreeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeFreeSlot
        fields=["free_day","free_time"]

class ClientDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClientDetails
        fields=["client_name","client_email","client_contact","client_password"]


