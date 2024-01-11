from rest_framework.response import Response
from rest_framework import viewsets
from .models import Schedule
from .serializer import ScheduleSerializer, ScheduleHistorySerializer


class ScheduleViewset(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Schedule.history.filter(id=pk)
        serializer = ScheduleHistorySerializer(queryset, many=True)
        return Response(serializer.data)
