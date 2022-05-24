from rest_framework.viewsets import ModelViewSet
from .serializer import AutorModelSerializer
from .models import Autor


class AutorModelViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorModelSerializer





