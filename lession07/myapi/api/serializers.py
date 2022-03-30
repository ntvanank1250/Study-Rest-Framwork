from rest_framework import serializers
from myapi.models import Customer

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =['name', 'email', 'address','phone']