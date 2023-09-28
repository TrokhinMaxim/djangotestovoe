from django.db import models
import datetime

POSSIBLE_MODELS = ["R2", "R3", "R4", "R5"]
POSSIBLE_VERSIONS = ["D2", "D3", "D4", "D5", "A1", "A2", "A3", "A4"]


class Robot(models.Model):
    serial = models.CharField(
        max_length=5, blank=False, null=False, verbose_name="Серия"
    )
    model = models.CharField(
        max_length=2, blank=False, null=False, verbose_name="Модель"
    )
    version = models.CharField(
        max_length=2, blank=False, null=False, verbose_name="Версия"
    )
    created = models.DateTimeField(
        blank=False, null=False, default=datetime.datetime.now, verbose_name="Создан"
    )

    def __str__(self):
        return f"{self.model}-{self.version}"
