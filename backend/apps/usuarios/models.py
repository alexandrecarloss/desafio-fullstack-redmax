from django.db import models

class Usuario(models.Model):
  nome = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  idade = models.PositiveIntegerField()
  created_at = models.DateTimeField(auto_now=True)