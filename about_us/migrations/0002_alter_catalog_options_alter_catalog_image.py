# Generated by Django 5.0.6 on 2024-06-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={'verbose_name': 'کاتالوک', 'verbose_name_plural': 'کاتالوگ ها'},
        ),
        migrations.AlterField(
            model_name='catalog',
            name='image',
            field=models.ImageField(upload_to='catalog_img/%y%m%d%H%M', verbose_name='عکس کاتالوگ'),
        ),
    ]