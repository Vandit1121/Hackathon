# Generated by Django 4.0.1 on 2022-03-27 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phoneNumber',
            field=models.CharField(max_length=15),
        ),
    ]