from django.db import models


class IssueTracker(models.Model):
    summary = models.CharField(verbose_name='Заголовок', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Подробное описание', max_length=500, null=True, blank=True)
    status = models.ManyToManyField('tracker.Status', related_name='statuses', blank=True)
    type = models.ManyToManyField('tracker.Type', related_name='types', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.summary}'


class Type(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Status(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'
