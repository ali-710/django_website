# Generated by Django 4.0 on 2022-01-22 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_contact_city_alter_contact_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
