from rest_framework import viewsets
from .models import StatusProcess as StatusUpcoming
from .serializer import StatusUpcomingSerializer


class StatusUpcomingViewset(viewsets.ModelViewSet):
    queryset = StatusUpcoming.objects.all()
    serializer_class = StatusUpcomingSerializer
