# Generated by Django 3.0.8 on 2020-08-10 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0048_daily_cart_newspaper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer_order',
            name='ac_no',
            field=models.CharField(max_length=32),
        ),
    ]
