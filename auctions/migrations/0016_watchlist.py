# Generated by Django 3.1 on 2020-08-26 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20200825_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auction_list')),
                ('bid_list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.bids')),
                ('comment_list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.comments')),
            ],
        ),
    ]