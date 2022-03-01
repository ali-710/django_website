# Generated by Django 4.0 on 2022-01-22 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]