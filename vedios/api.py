from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import VedioSerializer
from .models import Vedio


class VedioListAPI(generics.ListAPIView):
    queryset = Vedio.objects.all()
    serializer_class = VedioSerializer