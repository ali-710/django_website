# Generated by Django 4.0 on 2022-01-24 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='date',
            new_name='appointmentdate',
        ),
        migrations.RenameField(
            model_name='detail',
            old_name='time',
            new_name='appointmenttime',
        ),
    ]
