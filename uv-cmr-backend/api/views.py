from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


from .serializer import (
    EspecialidadSerializer, ProfesionalSerializer, TurnoSerializer, ProfesionalListSerializer,
    TurnoListSerializer, DisponibilidadSerializer, ConsultorioSerializer, 
    PacienteSerializer, ResultadoEstudioSerializer, ServicioSerializer, 
    ObraSocialSerializer, CategoriaServicioSerializer, 
)

from .models import (
    Especialidad, Profesional, Turno, Disponibilidad, Consultorio, 
    Paciente, ResultadoEstudio, Servicio, ObraSocial, CategoriaServicio
)

# ModelViewSet Hereda todos los mixins necesarios. Nos ahorra usar APIView

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ObraSocialViewSet(viewsets.ModelViewSet):
    queryset = ObraSocial.objects.all()
    serializer_class = ObraSocialSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ConsultorioViewSet(viewsets.ModelViewSet):
    queryset = Consultorio.objects.all()
    serializer_class = ConsultorioSerializer

class DisponibilidadViewSet(viewsets.ModelViewSet):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer




class ProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.all()
    
    # consulto listcon (get all). datos anidados 
    def get_serializer_class(self):
        if self.action == 'list':
            return ProfesionalListSerializer
        return ProfesionalSerializer


class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all().order_by('-fecha', '-hora')
    
    # filtros, ordenamientos y busquedas el cliente elige como vienen los datos
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
        ]
    filterset_fields = [
        'estado', 
        'profesional', 
        'fecha'
        ]
    search_fields = ['paciente__dni', 'paciente__usuario__last_name']
    ordering_fields = ['fecha', 'hora']

    
    def get_serializer_class(self):
        if self.action == 'list':
            return TurnoListSerializer
        return TurnoSerializer

    # funciones personalizadas

    @action (detail=True, methods=['delete'])
    def borrado_logico(self, request, pk=None):
        """Borro un turno, cambio el estado a 'cancelado'."""
        if (turno.estado == 'cancelado'):
            return Response({"status": "Error: Turno ya cancelado"}, status=400)

        turno = self.get_object()
        turno.estado = 'cancelado'
        turno.save()
        return Response({"status": "Turno borrado con éxito"})
   


    @action(detail=False, methods=['get'])
    def turnos_confirmados(self, request):
        turnos = Turno.objects.filter(estado='confirmado')
        page = self.paginate_queryset(turnos)

        if page is not None:
            serializer = TurnoListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
            
        serializer = TurnoListSerializer(turnos, many=True)
        return Response(serializer.data)
