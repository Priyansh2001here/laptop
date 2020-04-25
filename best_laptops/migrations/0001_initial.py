# Generated by Django 3.0.5 on 2020-04-25 06:10

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recommended', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_image', models.ImageField(upload_to='')),
                ('company_name', models.CharField(max_length=10)),
                ('company_desc', ckeditor.fields.RichTextField()),
                ('best_company', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NewLaptopReleases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laptop_name', models.CharField(max_length=50)),
                ('laptop_desc', models.CharField(max_length=200)),
                ('laptop_img', models.ImageField(upload_to='')),
                ('laptop_default_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laptop_name', models.CharField(max_length=50)),
                ('laptop_serial', models.CharField(max_length=30)),
                ('cost', models.IntegerField()),
                ('laptop_image', models.ImageField(null=True, upload_to='')),
                ('laptop_link_1', models.URLField(null=True)),
                ('laptop_link_2', models.URLField(null=True)),
                ('NewlyLaunched', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='recommended.Category')),
                ('company', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='best_laptops.Companies')),
            ],
        ),
    ]
