# Generated by Django 4.0.4 on 2022-05-08 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('cinema_code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(default='تهران', max_length=30)),
                ('capacity', models.IntegerField()),
                ('phone', models.CharField(max_length=20, null=True)),
                ('address', models.TextField()),
            ],
        ),
    ]
