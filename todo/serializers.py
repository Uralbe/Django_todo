from rest_framework import serializers
from .models import Todo

class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=("id", "title", "description", "status")
class UserProfileSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, required=False)
    class Meta:
        model = get_user_model()
        fields = "__all__"
