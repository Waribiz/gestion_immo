
from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'password', 'is_client', 'is_admin']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data.get('name'),
            is_client=validated_data.get('is_client', True),
            is_admin=validated_data.get('is_admin', False)
        )
        return user
