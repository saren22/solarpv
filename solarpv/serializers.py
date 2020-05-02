from rest_framework import serializers
from backend.models import Certificate

class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = ('certificate_number', 'id', 'report_number')


