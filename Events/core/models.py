from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Speaker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True)

    image = models.ImageField(upload_to='speaker')

    class Meta:
        verbose_name = 'Спикер'
        verbose_name_plural = 'Спикеры'

    def __str__(self):
        return f'Спикер {self.first_name} {self.last_name} <{self.pk}>'


class Topic(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return f'{self.title} id: {self.pk}'


class Location(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return f'{self.title} id: {self.pk}'


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='events')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='events', null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='events', null=True)

    event_date = models.DateTimeField()

    create_date = models.DateTimeField(auto_now=True)

    users = models.ManyToManyField(User, related_name='events', blank=True)
    speakers = models.ManyToManyField(Speaker, related_name='events')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['event_date', 'title']

    def __str__(self):
        return f'Событие {self.title} <{self.pk}>'
