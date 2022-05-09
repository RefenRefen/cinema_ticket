# Generated by Django 4.0.4 on 2022-05-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0004_alter_showtime_options_alter_cinema_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='status',
            field=models.IntegerField(choices=[(1, 'فروش آغاز نشده'), (2, 'در حال فروش بلیت'), (3, 'بلیت ها تمام شد.'), (4, 'فروش بلیت بسته شد.'), (5, 'فیلم پخش شد.'), (6, 'سانس لغو شد.')], verbose_name='وضعیت'),
        ),
    ]
