from ..models import CustomUser, HostUserProfile
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    event_hoster = serializers.StringRelatedField()
    
    class Meta:
        model = CustomUser 
        fields = ["id", "email", "password", "password2", "event_hoster"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
        
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("The two passwords do not match !")
        return data 
    
    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        confirm_account = CustomUser.objects.filter(email=email)
        if confirm_account.exists():
            raise serializers.ValidationError("An account already exists with this email")
        new_account = CustomUser.objects.create_user(email=email, password=password)
        return new_account
    

class HostUserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = HostUserProfile 
        fields = "__all__"
        