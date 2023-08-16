
from rest_framework import serializers
from .models import Name

class EventSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Name
        fields = '__all__'

    
