# Generated by Django 3.1 on 2020-08-28 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0026_comments_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='list_id',
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_list_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_list_id', to='auctions.auction_list'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user_id', to='auctions.auction_list'),
        ),
    ]