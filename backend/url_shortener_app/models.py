from django.db import models


class URL(models.Model):
    url = models.URLField(unique=True)

    def __str__(self):
        return self.url


class ShortLink(models.Model):
    url = models.OneToOneField(
        to=URL,
        on_delete=models.CASCADE,
        related_query_name='short'
    )

    short_link = models.CharField(max_length=10)

    def __str__(self):
        return f'ShortLink({self.url}): "{self.short_link}"'


class CustomShortLink(models.Model):
    url = models.ForeignKey(
        to=URL,
        on_delete=models.CASCADE,
        related_query_name='custom_short'
    )

    custom_short_link = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return f'CustomShortLink({self.url}): "{self.custom_short_link}"'
