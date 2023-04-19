from django.db import models
from django.db import models


class Menu(models.Model):
    "Создание меню"
    name = models.CharField(max_length=100, unique=True)
    slug=models.SlugField()
    url = models.CharField('Ссылка', max_length=255)

    class Meta:
        verbose_name = 'Mеню'
        verbose_name_plural = 'Mеню'

    def __str__(self):
        return str(self.name)

class MenuItem(models.Model):
    "Создание пункта выбранного меню"
    menu=models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu')
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=255)
    level = models.PositiveIntegerField(default=1)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        "Устанавливаем уровень вложенности при создании пункта меню"
        if self.parent:
            self.level = self.parent.level + 1
        else:
            self.level = 1
        super(MenuItem, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
