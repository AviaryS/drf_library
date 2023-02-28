from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    annotations = models.CharField(
        max_length=255, blank=True, default=""
    )
    published_date = models.DateField()
    author = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.author}: {self.name}'