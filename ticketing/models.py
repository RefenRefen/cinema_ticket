from django.db import models


# Create your models here.

class Movie(models.Model):
    """
    Represents a movie
    """
    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم'
    name = models.CharField(max_length=100, verbose_name='عنوان')
    director = models.CharField('کارگردان', max_length=50)
    year = models.IntegerField('سال')
    length = models.IntegerField('مدت زمان')
    description = models.TextField('توضیحات')

    def __str__(self):
        return self.name


class Cinema(models.Model):
    """
    Represents a cinema saloon
    """
    class Meta:
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'
    cinema_code = models.IntegerField(primary_key=True, verbose_name='کد سینما')
    name = models.CharField('نام', max_length=50)
    city = models.CharField('شهر', max_length=30, default='تهران')
    capacity = models.IntegerField('ظرفیت')
    phone = models.CharField('شماره تلقن', max_length=20, null=True)
    address = models.TextField('آدرس')

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    """
    Represents a movie show in a cinema a specific time
    """
    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس'

    movie = models.ForeignKey('Movie', on_delete=models.PROTECT)
    cinema = models.ForeignKey('Cinema', on_delete=models.PROTECT)
    start_time = models.DateTimeField('زمان شروع')
    price = models.IntegerField('قیمت')
    salable_seats = models.IntegerField('صندلی قابل فروش')
    free_seats = models.IntegerField('صندلی خالی', )

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choices = (
        (SALE_NOT_STARTED, 'فروش آغاز نشده'),
        (SALE_OPEN, 'در حال فروش بلیت'),
        (TICKETS_SOLD, 'بلیت ها تمام شد.'),
        (SALE_CLOSED, 'فروش بلیت بسته شد.'),
        (MOVIE_PLAYED, 'فیلم پخش شد.'),
        (SHOW_CANCELED, 'سانس لغو شد.')
    )
    status = models.IntegerField(choices=status_choices, verbose_name='وضعیت')

    def __str__(self):
        return '{} - {} - {}'.format(self.movie, self.cinema,
                                     self.start_time)
