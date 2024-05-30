from django.db import models


class IpsProjects(models.Model):
    project_title = models.CharField(max_length=30)
    project_time_city = models.CharField(max_length=33)
    project_address = models.CharField(max_length=66)
    project_main_image = models.ImageField(upload_to='img/%y%m%d%H%M')
    project_details = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    is_home_villa = models.BooleanField(default=False)
    is_facade = models.BooleanField(default=False)
    is_zero_to_hundred = models.BooleanField(default=False)
    is_coffe_restaurant = models.BooleanField(default=False)
    is_office = models.BooleanField(default=False)

    project_img_1 = models.ImageField(upload_to='img/%y%m%d%H%M', null=True, blank=True)
    project_img_2 = models.ImageField(upload_to='img/%y%m%d%H%M', null=True, blank=True)
    project_img_3 = models.ImageField(upload_to='img/%y%m%d%H%M', null=True, blank=True)
    project_img_4 = models.ImageField(upload_to='img/%y%m%d%H%M', null=True, blank=True)
    project_img_5 = models.ImageField(upload_to='img/%y%m%d%H%M', null=True, blank=True)
    project_img_6 = models.ImageField(upload_to='img/%y%m%d%H%M', null=True, blank=True)
