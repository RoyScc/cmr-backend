from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EspecialidadViewSet, ProfesionalViewSet, ServicioViewSet,
    ObraSocialViewSet, PacienteViewSet, ConsultorioViewSet,
    DisponibilidadViewSet, TurnoViewSet
)

router = DefaultRouter()
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'profesionales', ProfesionalViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'obras-sociales', ObraSocialViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'consultorios', ConsultorioViewSet)
router.register(r'disponibilidades', DisponibilidadViewSet)
router.register(r'turnos', TurnoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]