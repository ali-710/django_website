# Generated by Django 4.0 on 2022-01-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_rename_email_contact_city_remove_contact_msg_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(default='0', max_length=70),
        ),
    ]
