from django.urls import path
from .import views


urlpatterns=[
    path("services/",views.services, name="services"),
    path("appointment/",views.appointmentPage,name="appointment"),
    path("signup/",views.signup,name="signup-page"),
    path("login/",views.login,name="login"),
    path("appointment-slot/",views.displayFreeSlots,name="Free slots"),
]