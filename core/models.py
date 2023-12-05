from django.db import models


class CalculationResult(models.Model):
    id = models.AutoField(primary_key=True)
    result = models.IntegerField(null=True)
