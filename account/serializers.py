from rest_framework import serializers
from .models import User, Loan

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['approved_limit']

class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Loan
        fields = '__all__'
