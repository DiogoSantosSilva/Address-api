from django.db import models

class CountryModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StateModel(models.Model):
    name = models.CharField(max_length=255)
    state_acronym = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CityModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NeighbourhoodModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AddressModel(models.Model):
    street_name = models.CharField(max_length=255, blank=False)
    number = models.SmallIntegerField(blank=False)
    complement = models.CharField(max_length=255)
    neighbourhood = models.ForeignKey('NeighbourhoodModel', on_delete=models.CASCADE, blank=False)
    city = models.ForeignKey('CityModel', on_delete=models.CASCADE, blank=False)
    state = models.ForeignKey('StateModel', on_delete=models.CASCADE, blank=False)
    country = models.ForeignKey('CountryModel', on_delete=models.CASCADE, blank=False)
    zipcode = models.CharField(max_length=255, blank=False)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
