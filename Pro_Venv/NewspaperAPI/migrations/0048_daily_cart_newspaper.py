# Generated by Django 3.0.8 on 2020-08-08 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0047_auto_20200808_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_cart',
            name='newspaper',
            field=models.ManyToManyField(related_name='Consumer_ac_no', to='NewspaperAPI.Consumer_order'),
        ),
    ]