from rest_framework import serializers
from .models import GeeksModel


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeeksModel
        fields = '__all__'



