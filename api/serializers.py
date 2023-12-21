from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=500)
    message = serializers.CharField(max_length=5000)
    to_email = serializers.EmailField()