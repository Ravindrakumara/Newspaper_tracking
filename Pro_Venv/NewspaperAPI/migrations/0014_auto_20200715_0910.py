# Generated by Django 3.0.8 on 2020-07-15 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperAPI', '0013_auto_20200715_0543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='add_date',
            new_name='Create_date',
        ),
    ]
