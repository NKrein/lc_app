# Generated by Django 3.2.3 on 2021-05-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=15)),
                ('stock', models.IntegerField(max_length=10)),
                ('precio', models.CharField(max_length=5)),
            ],
        ),
    ]
