# Generated by Django 4.0 on 2022-01-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_blogpost_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=50)),
                ('city', models.TextField(max_length=250)),
                ('desc', models.CharField(max_length=250)),
            ],
        ),
    ]