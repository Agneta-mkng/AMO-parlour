from django.urls import path
from .import views
# the dot in the previous line shows that from this same project we are importing the views.

urlpatterns=[
    path("services/",views.services, name="services"),
]