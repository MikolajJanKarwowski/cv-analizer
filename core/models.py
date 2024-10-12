from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Usuario(AbstractUser):
    # Campos adicionales para el usuario
    telefono = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.username

    @classmethod
    def create_user(cls, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('El nombre de usuario es obligatorio')
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        
        user = cls(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class CV(models.Model):
    # Información personal
    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255, blank=True)
    #foto = models.ImageField(upload_to='fotos_cv/', blank=True, null=True)  # Requiere Pillow para gestionar imágenes
    fecha_nacimiento = models.DateField()

    # Resumen profesional
    perfil_profesional = models.TextField()

    # Experiencia laboral
    class Experiencia(models.Model):
        cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='experiencias')
        puesto = models.CharField(max_length=100)
        empresa = models.CharField(max_length=100)
        descripcion = models.TextField()
        fecha_inicio = models.DateField()
        fecha_fin = models.DateField(blank=True, null=True)
        ubicacion = models.CharField(max_length=100, blank=True)

        def __str__(self):
            return f"{self.puesto} en {self.empresa}"

    # Educación
    class Educacion(models.Model):
        cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='educacion')
        grado = models.CharField(max_length=100)
        institucion = models.CharField(max_length=100)
        fecha_inicio = models.DateField()
        fecha_fin = models.DateField(blank=True, null=True)
        descripcion = models.TextField(blank=True)

        def __str__(self):
            return f"{self.grado} en {self.institucion}"

    # Habilidades
    class Habilidad(models.Model):
        cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='habilidades')
        habilidad = models.CharField(max_length=100)
        descripcion = models.TextField(blank=True)

        def __str__(self):
            return self.habilidad

    # Certificaciones
    class Certificacion(models.Model):
        cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='certificaciones')
        titulo = models.CharField(max_length=100)
        institucion = models.CharField(max_length=100)
        fecha_obtencion = models.DateField()

        def __str__(self):
            return self.titulo

    # Idiomas
    class Idioma(models.Model):
        cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='idiomas')
        idioma = models.CharField(max_length=50)
        nivel = models.CharField(max_length=50)

        def __str__(self):
            return f"{self.idioma} ({self.nivel})"

    # Proyectos (opcional)
    class Proyecto(models.Model):
        cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='proyectos')
        titulo = models.CharField(max_length=100)
        descripcion = models.TextField()
        enlace = models.URLField(blank=True, null=True)

        def __str__(self):
            return self.titulo

    # Intereses (opcional)
    intereses = models.TextField(blank=True)

    def __str__(self):
        return self.nombre_completo