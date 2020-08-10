from django.test import TestCase
from django.urls import resolve
from rest_framework.test import APIClient
from address.models import CountryModel, StateModel, CityModel, NeighbourhoodModel, AddressModel
# Create your tests here.

class CountryTest(TestCase):

    def setUp(self):
        CountryModel.objects.create(name="brazil")
        CountryModel.objects.create(name="ireland")

    def test_get_country(self):
        country = CountryModel.objects.get(name="brazil")
        self.assertEqual('brazil', country.name)
        country = CountryModel.objects.get(name="ireland")
        self.assertEqual('ireland', country.name)

class StateTest(TestCase):

    def setUp(self):
        StateModel.objects.create(name="são paulo", state_acronym="sp")

    def test_get_country(self):
        state = StateModel.objects.get(state_acronym='sp')
        self.assertEqual('são paulo', state.name)

class CityTest(TestCase):

    def setUp(self):
        CityModel.objects.create(name="jaguariuna")

    def test_get_country(self):
        city = CityModel.objects.get(name="jaguariuna")
        self.assertEqual('jaguariuna', city.name)

class NeighbourhoodTest(TestCase):

    def setUp(self):
        NeighbourhoodModel.objects.create(name="recanto camanducaia")

    def test_get_country(self):
        neighbourhood = NeighbourhoodModel.objects.get(name="recanto camanducaia")
        self.assertEqual('recanto camanducaia', neighbourhood.name)

class AddressTest(TestCase):

    def setUp(self):
        country = CountryModel.objects.create(name="brazil")
        state = StateModel.objects.create(name="são paulo", state_acronym="sp")
        city = CityModel.objects.create(name="jaguariuna")
        neighbourhood = NeighbourhoodModel.objects.create(name="recanto camanducaia")
        AddressModel.objects.create(
            street_name="test", number=359, neighbourhood=neighbourhood,
            city=city, state=state, country=country, zipcode="13915001"
        )

    def test_get_country(self):
        address = AddressModel.objects.get(pk=1)
        self.assertEqual('test', address.street_name)
        self.assertEqual(359, address.number)
        self.assertEqual('brazil', address.country.name)
        self.assertEqual('sp', address.state.state_acronym)
        self.assertEqual('jaguariuna', address.city.name)
        self.assertEqual('recanto camanducaia', address.neighbourhood.name)





