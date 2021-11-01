from rest_framework import serializers

from admin_role.models import AdvisorModel
from .models import User,Booking


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=255,min_length=6,write_only=True)

    class Meta:
        model = User
        fields = ['id','email','password','username']

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)





class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=255,min_length=6,write_only=True)

    class Meta:
        model = User
        fields = ['id','email','password','token']

        read_only_fields = ['token']

class AdvisorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvisorModel
        fields = ['advisor_id','AdvisorName','AdvisorPhotoUrl']




class BookedCallsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = ['BookingTime','advisor_id','uid']

class BookingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['BookingId','BookingTime','advisor_id']