from rest_framework import serializers
from .models import *


class VedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vedio
        fields = '__all__'