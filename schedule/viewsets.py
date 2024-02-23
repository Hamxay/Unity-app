from rest_framework.response import Response
from rest_framework import viewsets
from .models import Schedule
from .serializer import ScheduleSerializer, ScheduleHistorySerializer


class ScheduleViewset(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        code = self.request.query_params.get('code')
        if code:
            queryset = Schedule.objects.filter(Code=code)
        else:
            queryset = Schedule.objects.all()
        return queryset


class ScheduleHistoryViewset(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Schedule.history.filter(id=pk)
        serializer = ScheduleHistorySerializer(queryset, many=True)
        return Response(serializer.data)
