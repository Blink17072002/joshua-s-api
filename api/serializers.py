from rest_framework import serializers
from .models import Models

class ModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models
        fields = ['id', 'name', 'year', 'description']