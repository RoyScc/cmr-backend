from django.db.models.functions import Upper
from django.db import models
from django.contrib.auth.models import User

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Profesional(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)
    nombre_completo = models.CharField(max_length=150)
    matricula = models.CharField(max_length=50, unique=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.nombre_completo

class CategoriaServicio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    categoria = models.ForeignKey(CategoriaServicio, on_delete=models.CASCADE, related_name='servicios')
    nombre = models.CharField(max_length=150)
    preparacion_previa = models.TextField(blank=True)
    duracion_min = models.IntegerField(default=30)

    def __str__(self):
        return self.nombre

class ObraSocial(models.Model):
    nombre = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20, blank=True)
    coseguro = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.SET_NULL, null=True, blank=True)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices = [('M', 'Masculino'), ('F', 'Femenino')])
    
    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name} - {self.dni}"

class Consultorio(models.Model):
    numero = models.CharField(max_length=10)
    piso = models.CharField(max_length=10)

    def __str__(self):
        return f"Consultorio {self.numero} - Piso {self.piso}"

class Disponibilidad(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='disponibilidades')
    consultorio = models.ForeignKey(Consultorio, on_delete=models.SET_NULL, null=True)
    dia_semana = models.IntegerField(choices=[(i, i) for i in range(1, 8)], help_text="1=Lunes, 7=Domingo")
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.profesional} - Día {self.dia_semana}"

class Turno(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
        ('completado', 'Completado'),
    )
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='turnos')
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    anotaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Turno {self.fecha} {self.hora} - {self.paciente}"

class ResultadoEstudio(models.Model):
    turno = models.OneToOneField(Turno, on_delete=models.CASCADE, related_name='resultado')
    informe_medico = models.TextField()
    diagnostico = models.TextField(blank=True, null=True)
    receta = models.TextField(blank=True, null=True)
    valores_espirometria = models.JSONField(null=True, blank=True)
    fecha_carga = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resultado Turno {self.turno.id}"