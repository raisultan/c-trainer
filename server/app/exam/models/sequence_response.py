from django.db import models


class SequenceResponse(models.Model):
    base_question = models.ForeignKey(
        to='exam.Sequence',
        on_delete=models.CASCADE,
        related_name='responses',
        verbose_name='Sequence Question',
    )
    number_in_seq = models.PositiveIntegerField(
        verbose_name='Number in sequence',
    )
