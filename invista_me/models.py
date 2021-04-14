from django.db import models
from datetime import datetime


#  armazenar ( investimento, valor, pago, data )
class Investimento(models.Model):
    investimento = models.TextField(max_length=255, verbose_name='investimento')
    valor = models.FloatField(verbose_name='valor')
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)

    # PARA NÃO APARECER ( investimento objects(1) )
    def __str__(self):
        return self.investimento
