from rest_framework.decorators import api_view,throttle_classes
from rest_framework.response import Response
from .serializer import ServiceSerializer,EmployeeFreeSlotSerializer,ApointmentSerializer,ClientDetailsSerializer
from .models import EmployeeFreeSlot,Services,Appointment,ClientDetails
from rest_framework import status
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.throttling import ScopedRateThrottle


#A view to display the services offered by the parlour.
@api_view(['GET'])
def services(request):
   all_ser=Services.objects.all() 
   serializer=ServiceSerializer(all_ser,many=True)
   return Response(serializer.data)


#A view to display free appointment slots
@api_view(['POST'])
def displayFreeSlots(request):
    appointment_date=request.data.get("appointment_date")

    if not appointment_date:
        return Response({"error":"Date is required"},status=status.HTTP_400_BAD_REQUEST)
    
    free_slots=EmployeeFreeSlot.objects.filter(free_day=appointment_date)
    serializer=EmployeeFreeSlotSerializer(free_slots,many=True)

    #Transformig the serializer data into to a simple list of strings for vue select down menu.
    available_times=[free_slots['free_time'] for slot in serializer.data if 'free_time' in slot]

    data={
        "message":"These are the free slots that you can schedule your appointment",
        "Slots are":available_times
    }
    return Response(data)


#A view to display appointment page
@api_view(['POST'])
def appointmentPage(request):
        client_email=request.data.get("client_email","")
        appointment_date=request.data.get("appointment_date","")
        appointment_time=request.data.get("appointment_time","")
        service_name=request.data.get("service","")

        #Save the data that you get from the user into your database
        new_appointment=Appointment(
            client_email=client_email,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            service_name=service_name,
        )
        new_appointment.save()
        taken_slot=EmployeeFreeSlot.objects.filter(free_day=appointment_date,free_time=appointment_time)

        if taken_slot.exists():
            taken_slot.delete()
            #When an user picks a free slot from the database,it is deleted to avoid double booking.
        return Response({
            "message":"Your appointment has been booked successfully!",
            "appointment_id":"generated_id"
            },status=status.HTTP_201_CREATED) 
    

    # A view for user signup
@api_view(['POST'])
def signup(request):
    client_email = request.data.get("client_email", "")
    client_name = request.data.get("client_name", "")
    client_contact = request.data.get("client_contact", "")
    client_password = request.data.get("client_password", "")

    # One email cannot be used to create multiple accounts.
    if ClientDetails.objects.filter(client_email=client_email).exists():
        return Response(
            {"error": "Kindly use another email address to sign up"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if len(client_password) >= 12:
        hashed_password = make_password(client_password)

        new_user = ClientDetails(
            client_email=client_email,
            client_name=client_name,
            client_contact=client_contact,
            client_password=hashed_password
        )

        new_user.save()

        return Response(
            {"message": "User profile created successfully"},
            status=status.HTTP_201_CREATED
        )

    else:
        return Response(
            {"message": "Password must be at least 12 characters"},
            status=status.HTTP_400_BAD_REQUEST
        )

#A view for user login
@api_view(['POST'])
@throttle_classes([ScopedRateThrottle])
def login(request):
    login.throttle_scope='login'
    client_email=request.data.get("client_email","")
    client_password=request.data.get("client_password","")
    try:
        user=ClientDetails.objects.get(client_email=client_email)

        if check_password(client_password,user.client_password):
            return Response({"message":"Successful login!"},status=status.HTTP_200_OK)
        else:
            return Response({"message":"Invalid login details!"},status=status.HTTP_401_UNAUTHORIZED)
    except ClientDetails.DoesNotExist:
        return Response({"message":"Invalid login detail!"},status=status.HTTP_401_UNAUTHORIZED)
    #For security reasons display invalid log in details so that a malicious person does not get to know of emails not found in the system.

    

