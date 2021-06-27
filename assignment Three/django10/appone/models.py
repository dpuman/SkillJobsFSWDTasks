from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    address = models.TextField(max_length=500, null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)

    def __str__(self):
        return self.name
