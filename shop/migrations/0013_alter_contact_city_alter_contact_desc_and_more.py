# Generated by Django 4.0 on 2022-01-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_contact_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=70),
        ),
    ]
