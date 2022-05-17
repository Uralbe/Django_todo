from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from todo.models import Todo
from  todo.serializers import Todoserializer
# Create your views here.

class TodoViewSet(ModelViewSet):
    serializer_class = Todoserializer
    authentication_classe = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    #queryset = Todo.objects.all()
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def preform_create(self, serializer):
        serializer.validated_data["user"]=self.request.user
        serializer.save()



