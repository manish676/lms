from rest_framework import serializers
from .models import Status

class StatusSerializers(serializers.ModelSerializers)
    class Meta:
        model = Status
        fields = ('__all__')
        