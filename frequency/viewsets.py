from rest_framework import viewsets
from .models import Frequency
from .serializer import FrequencySerializer


class FrequencyViewset(viewsets.ModelViewSet):
    queryset = Frequency.objects.all()
    serializer_class = FrequencySerializer
