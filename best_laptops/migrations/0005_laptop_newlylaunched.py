# Generated by Django 3.0.5 on 2020-04-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('best_laptops', '0004_auto_20200424_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='NewlyLaunched',
            field=models.BooleanField(default=False),
        ),
    ]