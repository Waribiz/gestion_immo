from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Contrat
from .serializers import ContratSerializer

class ContratViewSet(viewsets.ModelViewSet):
    queryset = Contrat.objects.all()
    serializer_class = ContratSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'client':
            return self.queryset.filter(client=user)
        return self.queryset  # admin peut voir tous les contrats

    def perform_create(self, serializer):
        if self.request.user.role == 'client':
            serializer.save(client=self.request.user)
        else:
            serializer.save()
