# Generated by Django 3.0.8 on 2020-08-17 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0049_auto_20200810_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_cart',
            name='ac_no',
            field=models.CharField(max_length=32),
        ),
        migrations.RemoveField(
            model_name='daily_cart',
            name='newspaper',
        ),
        migrations.AddField(
            model_name='daily_cart',
            name='newspaper',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
