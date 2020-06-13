from django.db import models


class Sequence(models.Model):
    base_question = models.OneToOneField(
        to='exam.Question',
        on_delete=models.CASCADE,
        related_name='sequence',
        verbose_name='Sequence Question',
    )
