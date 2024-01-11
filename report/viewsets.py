from rest_framework import viewsets
from .models import Report
from .serializer import ReportSerializer


class ReportViewset(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
