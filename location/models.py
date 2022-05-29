from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class Location(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    store_number = models.IntegerField(max_length=5)
    zone = models.IntegerField(max_length=2)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    def __str__(self):
        return self.name




