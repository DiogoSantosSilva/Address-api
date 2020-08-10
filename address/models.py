from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import requests

class CountryModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(CountryModel, self).save(*args, **kwargs)

class StateModel(models.Model):
    name = models.CharField(max_length=255)
    state_acronym = models.CharField(max_length=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(StateModel, self).save(*args, **kwargs)

class CityModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(CityModel, self).save(*args, **kwargs)

class NeighbourhoodModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(NeighbourhoodModel, self).save(*args, **kwargs)

class AddressModel(models.Model):
    street_name = models.CharField(max_length=255, null=False, blank=False)
    number = models.SmallIntegerField(null=False,blank=False)
    complement = models.CharField(max_length=255)
    neighbourhood = models.ForeignKey('NeighbourhoodModel', on_delete=models.CASCADE, null=False, blank=False)
    city = models.ForeignKey('CityModel', on_delete=models.CASCADE, null=False, blank=False)
    state = models.ForeignKey('StateModel', on_delete=models.CASCADE, null=False, blank=False)
    country = models.ForeignKey('CountryModel', on_delete=models.CASCADE, null=False, blank=False)
    zipcode = models.CharField(max_length=255,null=False, blank=False)
    latitude = models.CharField(max_length=255, blank=True)
    longitude = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.street_name} -  {self.number} - {self.city.name}/{self.state.state_acronym}'

    def save(self, *args, **kwargs):
        self.street_name = self.street_name.lower()
        self.complement = self.complement.lower()
        return super(AddressModel, self).save(*args, **kwargs)

@receiver(pre_save, sender=AddressModel)
def save_lat_long(sender, instance, *args, **kwargs):
    address = f'{instance.state}, {instance.city} '
    if not instance.latitude:
        instance.latitude = get_geocode(address)[0]
    if not instance.longitude:
        instance.longitude = get_geocode(address)[1]

def get_geocode(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address': address, "key": "AIzaSyDTK0igIQTCi5EYKL9tzOIJ9N6FUASGZos"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()['results']
        location = results[0]['geometry']['location']
        return location['lat'], location['lng']
    return None, None
