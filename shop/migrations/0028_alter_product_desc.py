# Generated by Django 4.0 on 2022-01-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_rename_date_detail_appointmentdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=2000),
        ),
    ]
