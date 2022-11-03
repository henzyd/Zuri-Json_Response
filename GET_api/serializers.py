from rest_framework import serializers


ENUM = (
    (0, 'addition'),
    (1, 'substraction'),
    (2, 'multiplication'),
)
class EnumSerializer(serializers.Serializer):
    operation_type = serializers.CharField(default=0, max_length=20)
    x = serializers.IntegerField()
    y = serializers.IntegerField()