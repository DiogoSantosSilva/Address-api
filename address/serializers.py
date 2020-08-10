from rest_framework import serializers
from address.models import CountryModel, StateModel, CityModel, NeighbourhoodModel, AddressModel

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = ["name"]

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateModel
        fields = ["name"]

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = ["name"]

class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighbourhoodModel
        fields = ["name"]

class AddressSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    state = StateSerializer()
    city = CitySerializer()
    neighbourhood = NeighbourhoodSerializer()
    class Meta:
        model = AddressModel
        fields = ["id", "street_name", "number", "complement", "neighbourhood",
                  "city", "state", "country", "zipcode", "latitude", "longitude", "created_at", "updated_at"]