from django.db import models

class Project(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.CharField("Описание", max_length=200)
    image = models.ImageField("Изоборажение", upload_to='main/images/')
    url = models.URLField("Ссылки", blank=True)

    def __str__(self):
        return self.title

    