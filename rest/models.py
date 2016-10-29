from django.db import models
from django.core.validators import MaxValueValidator
from rest_framework import serializers
# Create your models here.


class Resultado(models.Model):
    codigo = models.CharField(max_length=20)
    lectura_critica = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    matematicas = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    sociales = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    naturales = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    ingles = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    razonamiento_cuantitativo = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    competencias_ciudadanas = models.PositiveIntegerField(validators=[MaxValueValidator(100)])


# Serizalizador

class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = ('codigo', 'lectura_critica', 'matematicas', 'sociales', 'naturales', 'ingles',
                  'razonamiento_cuantitativo', 'competencias_ciudadanas',)


class ListResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = ('codigo', )