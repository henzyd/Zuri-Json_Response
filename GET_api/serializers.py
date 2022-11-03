from rest_framework import serializers
# from .models import EnumModel



ENUM = (
    (0, 'addition'),
    (1, 'substraction'),
    (2, 'multiplication'),
)
# class EnumSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EnumModel
#         fields = '__all__'


class EnumSerializer(serializers.Serializer):
    operation_type = serializers.CharField(max_length=50)
    x = serializers.IntegerField(default=0)
    y = serializers.IntegerField(default=0)