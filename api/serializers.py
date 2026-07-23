from rest_framework import serializers
from vegie.models import Receipe
from django.contrib.auth.models import User

class ReceipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipe
        fields = "__all__"
        read_only_fields = ["user"]
        

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password"
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)