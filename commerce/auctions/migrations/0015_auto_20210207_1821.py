# Generated by Django 3.1.5 on 2021-02-07 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20210207_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='startbid',
            field=models.IntegerField(),
        ),
    ]