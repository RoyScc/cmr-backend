from os import read
from rest_framework import serializers
from .models import (
    Especialidad, Profesional, CategoriaServicio, Servicio, 
    ObraSocial, Paciente, Consultorio, Disponibilidad, 
    Turno, ResultadoEstudio
)

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'

class CategoriaServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaServicio
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class ObraSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObraSocial
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    # Mostramos datos del User de Django de forma anidada
    nombre = serializers.CharField(source='usuario.first_name', read_only=True)
    apellido = serializers.CharField(source='usuario.last_name', read_only=True)
    email = serializers.EmailField(source='usuario.email', read_only=True)

    class Meta:
        model = Paciente
        fields = ['id', 'nombre', 'apellido', 'email', 'dni', 'telefono', 'obra_social']

class ConsultorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultorio
        fields = '__all__'

class DisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidad
        fields = '__all__'

class ResultadoEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoEstudio
        fields = '__all__'


class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = '__all__'

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'

# NESTED SERIALIZERS

class ProfesionalListSerializer(serializers.ModelSerializer):
    especialidad = EspecialidadSerializer(read_only=True)
    
    class Meta:
        model = Profesional
        fields = '__all__'

class TurnoListSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)
    profesional = ProfesionalSerializer(read_only=True)
    servicio = ServicioSerializer(read_only=True)
    consultorio = ConsultorioSerializer(read_only=True)

    class Meta:
        model = Turno
        fields = '__all__'