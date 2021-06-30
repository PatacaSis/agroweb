from django.db import models



#================= Modelo para Rubros, Subrubros y Umedida de gastos ==================
class RubroGasto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class RubroVenta(models.Model):
    nombre = models.CharField('Rubro de venta', max_length=100)

    class Meta:
        verbose_name='Rubro de venta'
        verbose_name_plural='Rubros de ventas'
        ordering=['nombre']

    def __str__(self):
        return self.nombre

class Subrubro(models.Model):
    nombre = models.CharField('Rubro', max_length=100)

    class Meta:
        verbose_name='Subrubro'
        verbose_name_plural='Sububros'
        ordering=['nombre']

    def __str__(self):
        return self.nombre

class Umedida(models.Model):
    nombre = models.CharField('Unidad de medida', max_length=20)

    class Meta:
        verbose_name='U.medida'
        verbose_name_plural='U.medidas'
        ordering=['nombre']

    def __str__(self):
        return self.nombre

#================= Modelo para Gastos de Mano de obra==================
class Empleado(models.Model):
    nombre = models.CharField('Nombre',max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    dni = models.CharField('Dni', max_length=10, unique=True)
    nacimiento = models.CharField('Fecha de nacimiento', max_length=50)
    domicilio = models.CharField('Domicilio', max_length=100)

    def __str__(self):
        return self.apellido + ', ' + self.nombre

    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        ordering = ['apellido']


CAT_EMPLEADO = (
    ('1','Encargado'),
    ('2', 'Ayudante'),
    ('3', 'Colaborador')
)

AREA = (
    ('1','Tambo'),
    ('2','Ganadería'),
    ('3','Estructura'),
    ('4','Tractorista'),
    ('5','General'),
)

class GastoMO(models.Model):
    fecha = models.DateField('Fecha de pago')
    nombre = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=1, choices=CAT_EMPLEADO)
    area = models.CharField(max_length=1, choices=AREA, verbose_name='Area de trabajo')
    salario = models.DecimalField(verbose_name='Salario', max_digits=9,decimal_places=2)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name='Gasto de Mano de Obra'
        verbose_name_plural='Gastos de Mano de Obra'

#================= Modelo para Gastos Generales==================
class Gasto(models.Model):
    fecha = models.DateField()
    comprobante = models.CharField(max_length=10)
    rubro = models.CharField(max_length=10,blank=True,null=True)
    subrubro = models.CharField(max_length=10)
    concepto = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    unidades = models.ForeignKey(Umedida, verbose_name='Unidad de medida', on_delete=models.CASCADE)
    importe = models.IntegerField()
    iva = models.IntegerField()

    class Meta:
        verbose_name='Gasto'
        verbose_name_plural='Gastos'
        ordering=['fecha']

    def __str__(self):
        return str(self.fecha)

    def imp_total(self):
        return self.importe + self.iva

    importe_total = property(imp_total)

#================= Modelo para Ventas==================
class Venta(models.Model):
    fecha = models.DateField()
    comprobante = models.CharField(max_length=10)
    rubro = models.ForeignKey(RubroVenta, on_delete=models.CASCADE, related_name='rubros')
    concepto = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    unidades = models.ForeignKey(Umedida, verbose_name='Unidad de medida', on_delete=models.CASCADE)
    importe = models.IntegerField()
    iva = models.IntegerField()

    class Meta:
        verbose_name='Venta'
        verbose_name_plural='Ventas'
        ordering=['fecha']

    def __str__(self):
        return str(self.fecha)

    def imp_total(self):
        return self.importe + self.iva

    importe_total = property(imp_total)

