from django.db import models


class ChoiceResponse(models.Model):
    base_question = models.ForeignKey(
        to='exam.Choice',
        on_delete=models.CASCADE,
        related_name='responses',
        verbose_name='Choice Question',
    )
    answer_id = models.PositiveIntegerField(
        verbose_name='Choice answer',
    )
