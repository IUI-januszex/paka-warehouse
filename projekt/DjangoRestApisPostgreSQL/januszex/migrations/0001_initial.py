# Generated by Django 3.2.8 on 2021-10-20 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalWarehouse',
            fields=[
                ('idGlobalWarehouse', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('numer', models.CharField(max_length=255)),
                ('postalCode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='LocalWarehouse',
            fields=[
                ('idLocalWarehouse', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=255)),
                ('ulica', models.CharField(max_length=255)),
                ('numer', models.CharField(max_length=255)),
                ('postalCode', models.CharField(max_length=6)),
                ('idGlobalWarehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='januszex.globalwarehouse')),
            ],
        ),
        migrations.CreateModel(
            name='RangePostalCode',
            fields=[
                ('idRangePostalCode', models.IntegerField(primary_key=True, serialize=False)),
                ('idLocalWarehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='januszex.localwarehouse')),
            ],
        ),
    ]