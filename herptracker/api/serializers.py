from rest_framework import serializers
from api.models import Herp, Observation

class HerpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Herp
        fields = [field.name for field in Herp._meta.get_fields() if field.concrete]

class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = [field.name for field in Observation._meta.get_fields() if field.concrete]