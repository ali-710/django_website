# Generated by Django 4.0 on 2022-01-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('comments', models.TextField(max_length=50)),
            ],
        ),
    ]