from django.db import models

# ============================
#        CONDUCTOR
# ============================
class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    licencia_conducir = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    estado_empleado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ============================
#          VEHICULO
# ============================
class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano_fabricacion = models.IntegerField()
    tipo_vehiculo = models.CharField(max_length=50)
    matricula = models.CharField(max_length=20)
    num_chasis = models.CharField(max_length=50)
    fecha_adquisicion = models.DateField()
    conductor_asignado = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    estado_vehiculo = models.CharField(max_length=50)
    kilometraje_actual = models.IntegerField()

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.matricula}"


# ============================
#        MANTENIMIENTO
# ============================
class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_mantenimiento = models.DateField()
    tipo_mantenimiento = models.CharField(max_length=100)
    costo_mantenimiento = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion_trabajo = models.TextField()
    proximo_mantenimiento = models.DateField()
    taller_mecanico = models.CharField(max_length=100)

    def __str__(self):
        return f"Mantenimiento {self.id} - {self.vehiculo}"


# ============================
#            RUTA
# ============================
class Ruta(models.Model):
    nombre_ruta = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    distancia_km = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_estimado_horas = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion_ruta = models.TextField()
    peajes_incluidos = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_ruta


# ============================
#            VIAJE
# ============================
class Viaje(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    fecha_inicio_viaje = models.DateTimeField()
    fecha_fin_viaje = models.DateTimeField()
    kilometraje_inicio = models.IntegerField()
    kilometraje_fin = models.IntegerField()
    combustible_gastado = models.DecimalField(max_digits=10, decimal_places=2)
    comentarios = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Viaje {self.id}"


# ============================
#         GASOLINA
# ============================
class Gasolina(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_recarga = models.DateTimeField()
    cantidad_litros = models.DecimalField(max_digits=8, decimal_places=2)
    precio_litro = models.DecimalField(max_digits=5, decimal_places=2)
    total_gasto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_combustible = models.CharField(max_length=50)
    estacion_servicio = models.CharField(max_length=100)
    kilometraje_recarga = models.IntegerField()

    def __str__(self):
        return f"Recarga {self.id} - {self.vehiculo}"


# ============================
#           SEGURO
# ============================
class Seguro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    numero_poliza = models.CharField(max_length=50)
    fecha_inicio_poliza = models.DateField()
    fecha_fin_poliza = models.DateField()
    compania_seguros = models.CharField(max_length=100)
    tipo_cobertura = models.CharField(max_length=100)
    costo_anual = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago_renovacion = models.DateField()

    def __str__(self):
        return f"Seguro {self.numero_poliza}"
