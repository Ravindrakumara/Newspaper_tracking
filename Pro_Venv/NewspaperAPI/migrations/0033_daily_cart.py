# Generated by Django 3.0.8 on 2020-07-31 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0032_auto_20200730_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(auto_now_add=True, max_length=32)),
                ('ac_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewspaperAPI.Consumer')),
                ('newspaper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewspaperAPI.Order')),
            ],
        ),
    ]