# Generated by Django 3.1 on 2020-08-30 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0029_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]