# Generated by Django 3.2.8 on 2021-12-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('januszex', '0005_alter_globalwarehouse_idglobalwarehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localwarehouse',
            name='idLocalWarehouse',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
