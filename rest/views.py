from rest.models import Resultado, ResultadoSerializer, ListResultadoSerializer
from rest_framework import mixins, viewsets
# Create your views here.


class ResultadoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer

    def list(self, request, *args, **kwargs):
        #  Parametro codigo
        if 'codigo' in request.query_params:
            codigo = request.query_params.get('codigo')
            self.queryset = self.queryset.filter(codigo=codigo)
        else:
            # Listado de codigos unicamente
            self.serializer_class = ListResultadoSerializer
        return super(ResultadoViewSet, self).list(request, *args, **kwargs)
