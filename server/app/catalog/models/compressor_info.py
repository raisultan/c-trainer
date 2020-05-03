from django.db import models


class CompressorInfo(models.Model):
    author = models.ForeignKey(
        to='users.BaseUser',
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='Author',
    )
    image = models.ImageField(
        upload_to='compressors/',
        blank=True,
        null=True,
        verbose_name='Image',
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Title',
    )
    text = models.TextField(
        verbose_name='Text',
    )
