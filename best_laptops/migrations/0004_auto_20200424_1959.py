# Generated by Django 3.0.5 on 2020-04-24 14:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best_laptops', '0003_auto_20200424_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='company_desc',
            field=ckeditor.fields.RichTextField(),
        ),
    ]