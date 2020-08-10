from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from address.models import (CountryModel, StateModel, CityModel,
                            NeighbourhoodModel, AddressModel)
from address.serializers import (CountrySerializer, StateSerializer, CitySerializer,
                                 NeighbourhoodSerializer, AddressSerializer)

class CountryListView(APIView):
    def get(self, request):
        obj = CountryModel.objects.all()
        serializer = CountrySerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CountryView(APIView):

    def get_object(self, pk):
        try:
            return CountryModel.objects.get(pk=pk)
        except CountryModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            obj = CountryModel.objects.get(pk=pk)
            serializer = CountrySerializer(obj)
            return Response(serializer.data)
        except CountryModel.DoesNotExist:
            raise Http404

    #usuarios não devem executar esta ação
    # def put(self, request, pk):
    #     obj = self.get_object(pk)
    #     serializer = CountrySerializer(obj, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk):
    #     obj = self.get_object(pk)
    #     obj.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class StateListView(APIView):
    def get(self, request):
        obj = StateModel.objects.all()
        serializer = StateSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StateView(APIView):
    def get_object(self, pk):
        try:
            return StateModel.objects.get(pk=pk)
        except StateModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            obj = StateModel.objects.get(pk=pk)
            serializer = StateSerializer(obj)
            return Response(serializer.data)
        except StateModel.DoesNotExist:
            raise Http404

    # usuarios não devem executar esta ação
    # def put(self, request, pk):
    #     obj = self.get_object(pk)
    #     serializer = StateSerializer(obj, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk):
    #     obj = self.get_object(pk)
    #     obj.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class CityListView(APIView):
    def get(self, request):
        obj = CityModel.objects.all()
        serializer = CitySerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CityView(APIView):

    def get_object(self, pk):
        try:
            return CountryModel.objects.get(pk=pk)
        except CountryModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            obj = CityModel.objects.get(pk=pk)
            serializer = CitySerializer(obj)
            return Response(serializer.data)
        except CityModel.DoesNotExist:
            raise Http404

    # # usuarios não devem executar esta ação
    # def put(self, request, pk):
    #     obj = self.get_object(pk)
    #     serializer = CitySerializer(obj, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk):
    #     obj = self.get_object(pk)
    #     obj.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class NeighbourhoodListView(APIView):
    def get(self, request):
        obj = NeighbourhoodModel.objects.all()
        serializer = NeighbourhoodSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NeighbourhoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NeighbourhoodView(APIView):
    def get_object(self, pk):
        try:
            return NeighbourhoodModel.objects.get(pk=pk)
        except NeighbourhoodModel.DoesNotExist:
            raise Http404

    def get(self, request, name):
        try:
            obj = NeighbourhoodModel.objects.get(name=name)
            serializer = NeighbourhoodSerializer(obj)
            return Response(serializer.data)
        except NeighbourhoodModel.DoesNotExist:
            raise Http404

    # usuarios não devem executar esta ação
    # def put(self, request, pk):
    #     obj = self.get_object(pk)
    #     serializer = NeighbourhoodSerializer(obj, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk):
    #     obj = self.get_object(pk)
    #     obj.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class AddressListView(APIView):
    def get(self, request):
        obj = AddressModel.objects.all()
        serializer = AddressSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        street_name = request.data.get('street_name')
        number = request.data.get('number')
        complement = request.data.get('complement')
        zipcode = request.data.get('zipcode')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        if 'name' in request.data.get('country'):
            country = CountryModel.objects.get_or_create(name=request.data.get('country')['name'])[0]
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if 'name' in request.data.get('state'):
            state = StateModel.objects.get_or_create(name=request.data.get('state')['name'])[0]
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if 'name' in request.data.get('city'):
            city = CityModel.objects.get_or_create(name=request.data.get('city')['name'])[0]
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if 'name' in request.data.get('neighbourhood'):
            neighbourhood = NeighbourhoodModel.objects.get_or_create(name=request.data.get('neighbourhood')['name'])[0]
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        address = AddressModel.objects.create(
            street_name=street_name, number=number, complement=complement, neighbourhood=neighbourhood, city=city,
            state=state, country=country, zipcode=zipcode, latitude=latitude, longitude=longitude
        )
        serializer = AddressSerializer(address)
        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressView(APIView):

    def get_object(self, pk):
        try:
            return AddressModel.objects.get(pk=pk)
        except AddressModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = AddressSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        obj.street_name = request.data.get('street_name')
        obj.number = request.data.get('number')
        obj.complement = request.data.get('complement')
        obj.zipcode = request.data.get('zipcode')
        obj.latitude = request.data.get('latitude')
        obj.longitude = request.data.get('longitude')
        if 'name' in  request.data.get('country'):
            obj.country = CountryModel.objects.get_or_create(name=request.data.get('country')['name'])[0]
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if 'name' in request.data.get('state'):
            obj.state = StateModel.objects.get_or_create(name=request.data.get('state')['name'])[0]
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if 'name' in request.data.get('city'):
            obj.city = CityModel.objects.get_or_create(name=request.data.get('city')['name'])[0]
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if 'name' in request.data.get('neighbourhood'):
            obj.neighbourhood = NeighbourhoodModel.objects.get_or_create(name=request.data.get('neighbourhood')['name'])[0]
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        obj.save()

        serializer = AddressSerializer(obj)
        if serializer:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)