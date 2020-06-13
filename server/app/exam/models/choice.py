from django.db import models


class Choice(models.Model):
    base_question = models.OneToOneField(
        to='exam.Question',
        on_delete=models.CASCADE,
        related_name='choice',
        verbose_name='Choice Question',
    )
