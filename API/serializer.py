from rest_framework import serializers
from .models import Order
from .models import Resources

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        # fields = ('')
        fields = ('__all__')

class ResourcesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resources
        #fields = ('')
        fields = ('__all__')

# Converts to JSON
# Validation
