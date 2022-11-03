from rest_framework import serializers
from .models import EnumModel



ENUM = (
    (0, 'addition'),
    (1, 'substraction'),
    (2, 'multiplication'),
)
class EnumSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnumModel
        fields = '__all__'