from rest_framework.viewsets import ModelViewSet
from core.models import editora
from core.serializers import EditoraSerializer

class EditoraViewSet(ModelViewSet):
    queryset = editora.objects.all()
    serializer_class = EditoraSerializer  