# Generated by Django 5.0.6 on 2024-06-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction_cost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='constructioncost',
            name='last_prices_update',
            field=models.CharField(blank=True, max_length=33, null=True, verbose_name='اخرین بروز رسانی'),
        ),
    ]
