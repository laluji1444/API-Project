from rest_framework import viewsets # This Viewset is use to like listing, creating, retrieving, updating, and deleting
from DeepApp.models import Name
from .serializers import EventSerializer


# Create your views here.

class EventView(viewsets.ModelViewSet):# This viewsets.ModelViewSet handles CRUD operations (Create, Read, Update, Delete) for the Name model.
     
    queryset = Name.objects.all()
    serializer_class = EventSerializer
    
   