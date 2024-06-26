from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customizes JWT default Serializer to add more information about user"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, min_length=4, write_only=True)
    email=serializers.EmailField(max_length=255, min_length=6)
    first_name=serializers.CharField(max_length=255, min_length=1)
    last_name=serializers.CharField(max_length=255, min_length=1)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"Email": "Email taken"})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"Username": "Username taken"})
        return super().validate(args)
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
#Change Password/reset
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
