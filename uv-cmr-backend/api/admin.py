from django.contrib import admin
from .models import (
    Especialidad, Profesional, CategoriaServicio, Servicio, 
    ObraSocial, Paciente, Consultorio, Disponibilidad, 
    Turno, ResultadoEstudio
)

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora', 'paciente', 'profesional', 'estado')
    list_filter = ('estado', 'fecha', 'profesional')
    search_fields = ('paciente__dni', 'paciente__usuario__last_name', 'profesional__nombre_completo')
    ordering = ('-fecha', '-hora')

@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'especialidad', 'matricula')
    list_filter = ('especialidad',)
    search_fields = ('nombre_completo', 'matricula')
    ordering = ('nombre_completo',)

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'dni', 'obra_social', 'telefono')
    list_filter = ('obra_social',)
    search_fields = ('dni', 'usuario__first_name', 'usuario__last_name')


admin.site.register(Especialidad)
admin.site.register(CategoriaServicio)
admin.site.register(Servicio)
admin.site.register(ObraSocial)
admin.site.register(Consultorio)
admin.site.register(Disponibilidad)
admin.site.register(ResultadoEstudio)