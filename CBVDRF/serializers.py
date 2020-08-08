from rest_framework import serializers

from CBVDRF.models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ['id', 'name', 'age']
