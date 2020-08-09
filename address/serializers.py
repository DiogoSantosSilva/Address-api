from rest_framework import serializers
from address.models import CountryModel, StateModel, CityModel, NeighbourhoodModel, AddressModel

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CountryModel
        fields = ['*']

class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StateModel
        fields = ['*']

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CityModel
        fields = ['*']

class NeighbourhoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NeighbourhoodModel
        fields = ['*']

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressModel
        fields = ['*']