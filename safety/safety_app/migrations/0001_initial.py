# Generated by Django 3.0.8 on 2020-08-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('Image', models.ImageField(upload_to='pics')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('Discount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('slug', models.SlugField(max_length=80)),
                ('Brand_Name', models.CharField(max_length=80)),
                ('Category_Name', models.CharField(max_length=80)),
                ('Colour', models.CharField(max_length=80)),
                ('Size', models.CharField(max_length=80)),
                ('Weight', models.FloatField()),
                ('Discription', models.TextField(max_length=80)),
                ('Modify_date', models.DateTimeField()),
                ('Expiry_date', models.DateTimeField()),
                ('Create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
