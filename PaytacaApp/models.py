from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    website_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gmap_business_link = models.URLField(blank=True, null=True)
    last_transaction_date = models.DateTimeField(blank=True, null=True)
    receiving_pubkey = models.CharField(max_length=255, blank=True, null=True)
    receiving_address = models.CharField(max_length=255, blank=True, null=True)

class Vault(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True)
    token_address = models.CharField(max_length=255, null=True)

class Logo(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, null=True)
    url = models.URLField(null=True)
