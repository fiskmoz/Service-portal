from rest_framework import serializers
from .models import Order
from .models import NewResource
from .models import SystemIdentif, Agreements

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        # fields = ('')
        fields = ('__all__')

class NewResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewResource
        fields = ('__all__')

class SystemIdentifSerializer(serializers.ModelSerializer):

    class Meta:
        model = SystemIdentif
        fields = ('__all__')

class AgreementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreements
        fields = ('__all__')

# Converts to JSON
# Validation
