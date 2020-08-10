import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from address.models import CountryModel, StateModel, CityModel, NeighbourhoodModel, AddressModel
from address.serializers import AddressSerializer

client = Client()

class GetAllAddressTest(TestCase):
    
    def setUp(self):
        country = CountryModel.objects.create(name="brazil")
        state = StateModel.objects.create(name="são paulo", state_acronym="sp")
        city = CityModel.objects.create(name="jaguariuna")
        neighbourhood = NeighbourhoodModel.objects.create(name="recanto camanducaia")
        AddressModel.objects.create(
            street_name="street of test", number=222, neighbourhood=neighbourhood,
            city=city, state=state, country=country, zipcode="13915001"
        )

        neighbourhood = NeighbourhoodModel.objects.create(name="centro")
        AddressModel.objects.create(
            street_name="street unit test", number=111, neighbourhood=neighbourhood,
            city=city, state=state, country=country, zipcode="13915001"
        )
        city = CityModel.objects.create(name="amparo")
        neighbourhood = NeighbourhoodModel.objects.create(name="sao dimas")
        AddressModel.objects.create(
            street_name="street integration test", number=333, neighbourhood=neighbourhood,
            city=city, state=state, country=country, zipcode="13915001"
        )
        
    def test_get_all_address(self):
        response = client.get(reverse('get_all_address'))
        addresses = AddressModel.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_firt_address(self):
        response = client.get(reverse('get_address',  kwargs={'pk': 1}))
        addresses = AddressModel.objects.get(pk=1)
        serializer = AddressSerializer(addresses)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_address(self):
        response = client.get(reverse('get_address',  kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateAddressTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            "street_name": "Rua: Paulo Eiró",
            "number": 55,
            "complement": "teste",
            "neighbourhood": {
                "name": "recanto camanducaia"
            },
            "city": {
                "name":"sao paulo"
            },
            "state": {
                "name": "sao paulo"
            },
            "country": {
                "name": "brasil"
            },
            "zipcode": "13060226",
            "latitude": "222",
            "longitude": "2222"
        }

        self.valid_payload_lat_long = {
            "street_name": "Rua: Paulo Eiró",
            "number": 55,
            "complement": "teste",
            "neighbourhood": {
                "name": "recanto camanducaia"
            },
            "city": {
                "name": "sao paulo"
            },
            "state": {
                "name": "sao paulo"
            },
            "country": {
                "name": "brasil"
            },
            "zipcode": "13060226",
        }

        self.invalid_payload = {
            "street_name": "Rua: Paulo Eiró",
            "number": 55,
            "complement": "teste",
            "neighbourhood":  "recanto camanducaia",
            "city":  "sao paulo",
            "state": "sao paulo",
            "country":  "brasil",
            "zipcode": "13060226",
            "latitude": "222",
            "longitude": "2222"
        }

    def test_create_valid_address(self):
        response = client.post(reverse('get_all_address'), data=json.dumps(self.valid_payload),
                               content_type="application/json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_address(self):
        response = client.post(reverse('get_all_address'), data=json.dumps(self.invalid_payload),
                               content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_address_lat_long(self):
        response = client.post(reverse('get_all_address'), data=json.dumps(self.valid_payload_lat_long),
                               content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data.get('latitude'))
        self.assertIsNotNone(response.data.get('longitude'))


class UpdateAddressTest(TestCase):
    def setUp(self):
        country = CountryModel.objects.create(name="brazil")
        state = StateModel.objects.create(name="são paulo", state_acronym="sp")
        city = CityModel.objects.create(name="jaguariuna")
        neighbourhood = NeighbourhoodModel.objects.create(name="recanto camanducaia")
        AddressModel.objects.create(
            street_name="street of test", number=222, neighbourhood=neighbourhood,
            city=city, state=state, country=country, zipcode="13915001"
        )

        self.valid_payload = {
            "street_name": "Rua: Paulo Eiró",
            "number": 55,
            "complement": "teste",
            "neighbourhood": {
                "name": "recanto camanducaia"
            },
            "city": {
                "name": "sao paulo"
            },
            "state": {
                "name": "sao paulo"
            },
            "country": {
                "name": "brasil"
            },
            "zipcode": "13060226",
            "latitude": "222",
            "longitude": "2222"
        }

        self.invalid_payload = {
            "street_name": "Rua: Paulo Eiró",
            "number": 55,
            "complement": "teste",
            "neighbourhood": "recanto camanducaia",
            "city": "sao paulo",
            "state": "sao paulo",
            "country": "brasil",
            "zipcode": "13060226",
            "latitude": "222",
            "longitude": "2222"
        }

    def test_update_valid_address(self):
        response = client.put(reverse('get_address', kwargs={'pk': 1}),
                              data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_invalid_address(self):
        response = client.put(reverse('get_address', kwargs={'pk': 1}),
                              data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteAddressTest(TestCase):
    def setUp(self):
        country = CountryModel.objects.create(name="brazil")
        state = StateModel.objects.create(name="são paulo", state_acronym="sp")
        city = CityModel.objects.create(name="jaguariuna")
        neighbourhood = NeighbourhoodModel.objects.create(name="recanto camanducaia")
        AddressModel.objects.create(
            street_name="street of test", number=222, neighbourhood=neighbourhood,
            city=city, state=state, country=country, zipcode="13915001"
        )

    def test_delete_address(self):
        response = client.delete(reverse('get_address', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_address(self):
        response = client.delete(reverse('get_address', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

