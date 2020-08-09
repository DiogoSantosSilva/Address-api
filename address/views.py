from rest_framework import viewsets
from address.models import (CountryModel, StateModel, CityModel,
                            NeighbourhoodModel, AddressModel)
from address.serializers import (CountrySerializer, StateSerializer, CitySerializer,
                                 NeighbourhoodSerializer, AddressSerializer)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = CountryModel.objects.all()
    serializer_class = CountrySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = StateModel.objects.all()
    serializer_class = StateSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = CityModel.objects.all()
    serializer_class = CitySerializer

class NeighbourhoodViewSet(viewsets.ModelViewSet):
    queryset = NeighbourhoodModel.objects.all()
    serializer_class = NeighbourhoodSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer