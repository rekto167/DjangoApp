# Generated by Django 3.1.5 on 2021-01-25 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0010_auto_20210125_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='food_cat',
            field=models.CharField(choices=[('minuman', 'Minuman'), ('makanan', 'Makanan')], max_length=100),
        ),
    ]