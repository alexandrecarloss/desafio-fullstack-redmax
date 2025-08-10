from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = '__all__'

  def validate_nome(self, value):
    if len(value) < 2:
      raise serializers.ValidationError("O nome deve ter pelo menos 2 caracteres.")
    return value

  def validate_idade(self, value):
    if value < 1 or value > 120:
      raise serializers.ValidationError("A idade deve estar entre 1 e 120.")
    return value
  
  def validate_email(self, value):
    if Usuario.objects.filter(email=value).exists():
        raise serializers.ValidationError("Este e-mail já está cadastrado.")
    return value


 