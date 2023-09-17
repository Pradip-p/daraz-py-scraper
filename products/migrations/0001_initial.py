# Generated by Django 4.2.1 on 2023-09-17 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('rating', models.CharField(max_length=200, null=True)),
                ('price', models.CharField(max_length=200)),
                ('reviews', models.CharField(max_length=200, null=True)),
                ('sold_by', models.CharField(max_length=200)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]