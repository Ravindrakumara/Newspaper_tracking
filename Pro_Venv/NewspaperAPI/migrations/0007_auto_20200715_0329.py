# Generated by Django 3.0.8 on 2020-07-14 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0006_auto_20200714_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspaper',
            name='lang',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newspaper',
            name='publication',
            field=models.TextField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newspaper',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
