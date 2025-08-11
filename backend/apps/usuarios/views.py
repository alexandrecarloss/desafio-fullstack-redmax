from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def list(self, request, *args, **kwargs):
        usuarios = self.get_queryset()
        serializer = self.get_serializer(usuarios, many=True)
        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()
        return Response({
            "success": True,
            "message": "Usuário criado com sucesso",
            "data": self.get_serializer(usuario).data
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        usuario = self.get_object()
        serializer = self.get_serializer(usuario)
        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        usuario = self.get_object()
        serializer = self.get_serializer(usuario, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "success": True,
            "message": "Usuário atualizado com sucesso",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        usuario = self.get_object()
        usuario.delete()
        return Response({
            "success": True,
            "message": "Usuário deletado com sucesso"
        }, status=status.HTTP_204_NO_CONTENT)
