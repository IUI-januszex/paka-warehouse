# Generated by Django 3.2.8 on 2021-10-20 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('januszex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangepostalcode',
            name='idRangePostalCode',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
