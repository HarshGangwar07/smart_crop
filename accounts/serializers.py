from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User

#class LoginSerializer(serializers.Serializer):
 #   username = serializers.CharField()
  #  password = serializers.CharField(write_only=True)

   # def validate(self, data):
    #    user = authenticate(username=data['username'], password=data['password'])
     #   if user and user.is_active:
      #      data['user']= user
       #     return data
        #raise serializers.ValidationError("Invalid username or password")
    
# ✅ Serializer for Register API
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
