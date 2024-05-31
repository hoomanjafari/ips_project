from django.db import models


class Catalog(models.Model):
    image = models.ImageField(upload_to='catalog_img/%y%m%d%H%M')
