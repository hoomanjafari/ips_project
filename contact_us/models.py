from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=66)
    number = models.CharField(max_length=14)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'( {self.name} ) -- ( {self.number} )'
