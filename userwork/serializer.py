from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Autor


class AutorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        # При выборе связного с User поля user = models.OneToOneField(User, on_delete=models.CASCADE)
        # возникает ошибка, поэтому убрал тут поле - 'user'
        fields = ('first_name', 'last_name', 'email_autor')
        # fields = '__all__'
