from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ServiceSerializer,EmployeeFreeSlotSerializer,ApointmentSerializer
from .models import EmployeeFreeSlot,Service,Appointment
from rest_framework import status


#A view to display the services offered by the parlour.
@api_view(['GET'])
def services(request):
   all_ser=services.object.all() 
   context={
       "message":"These are the services offered by AMO parlour",
       "Services":all_ser
   }
   return(Response,context)


#A view to display free appointment slots
@api_view(['GET'])
def displayFreeSlots(request):
    free_slots=EmployeeFreeSlot.object.all()
    serializer=EmployeeFreeSlotSerializer(free_slots,many=True)

    data={
        "message":"These are the free slots that you can schedule your appointment",
        "Slots are":serializer.data
    }
    return Response(data)


#A view to display appointment page
@api_view(['GET','POST'])
def appointmentPage(request):
    if request.method=='GET':
        app=Appointment.object.all()
        serializer=ApointmentSerializer(app,many=True)
        data={
            "Message":"Welcome 😊.You can book an appointment at your own convenience",
            "Booking":serializer.data
        }
        return Response(data)

    elif request.method=='POST':
        client_email=request.data.get("client_email","")
        appointment_date=request.data.get("appointment_date","")
        appointment_time=request.data.get("appointment_time","")
        service=request.data.get("service","")

        #Save the data that you get from the user into your database
        new_appointment=Appointment(
            client_email=client_email,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            service=service
        )
        return Response({
            "message":"Your appointment has been booked successfully!" 
            },status=status.HTTP_201_CREATED) 

