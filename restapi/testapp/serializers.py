from rest_framework import serializers
from  testapp.models import  student

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"