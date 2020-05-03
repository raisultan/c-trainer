from django.db import models


class Trainer(models.Model):
    user = models.OneToOneField(
        to='users.BaseUser',
        on_delete=models.CASCADE,
        related_name='trainer',
        verbose_name='Base User',
    )
