# Generated by Django 4.0.4 on 2022-05-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0003_alter_cinema_options_alter_movie_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='showtime',
            options={'verbose_name': 'سانس', 'verbose_name_plural': 'سانس'},
        ),
        migrations.AlterField(
            model_name='cinema',
            name='address',
            field=models.TextField(verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='capacity',
            field=models.IntegerField(verbose_name='ظرفیت'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='cinema_code',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='کد سینما'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='city',
            field=models.CharField(default='تهران', max_length=30, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='name',
            field=models.CharField(max_length=50, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='شماره تلقن'),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='free_seats',
            field=models.IntegerField(verbose_name='صندلی خالی'),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='salable_seats',
            field=models.IntegerField(verbose_name='صندلی قابل فروش'),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='start_time',
            field=models.DateTimeField(verbose_name='زمان شروع'),
        ),
    ]
