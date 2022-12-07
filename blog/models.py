from django.db import models

class Blog(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField("Описание")
    date = models.DateField("Дата")

    def __str__(self):
        return self.title

    