# Generated by Django 5.0.6 on 2024-05-25 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_merchants_merchant'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='last_update',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='watchtower_merchant_id',
            field=models.IntegerField(null=True),
        ),
    ]
