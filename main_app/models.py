from django.db import models

# Create your models here.
class Nft(models.Model):
  collection_name = models.CharField(max_length=100)
  floor_price = models.FloatField()

  def __str__(self):
    return f'{self.collection_name} ({self.id})'