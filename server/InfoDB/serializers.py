from rest_framework import serializers
from InfoDB.models import Lead
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lead
        fields='__all__'