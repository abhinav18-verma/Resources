from rest_framework import serializers
from .models import InvestorResource

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorResource
        fields = ['id', 'prompt', 'articles', 'videos']