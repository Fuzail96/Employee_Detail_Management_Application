# Generated by Django 3.0.8 on 2020-07-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=20)),
                ('fName', models.CharField(max_length=40)),
                ('lName', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=40)),
            ],
        ),
    ]
