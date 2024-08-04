from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = '__all__'
        extra_kwargs = {'short_url': {'required': False}}  # Ensure it's not required
