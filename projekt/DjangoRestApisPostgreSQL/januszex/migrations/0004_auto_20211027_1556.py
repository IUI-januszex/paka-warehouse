# Generated by Django 3.2.8 on 2021-10-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('januszex', '0003_auto_20211020_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalwarehouse',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='localwarehouse',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
