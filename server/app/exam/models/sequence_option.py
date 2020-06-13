from django.db import models


class SequenceOption(models.Model):
    question = models.ForeignKey(
        to='exam.Sequence',
        on_delete=models.CASCADE,
        related_name='options',
        verbose_name='Question',
    )
    title = models.CharField(
        max_length=214,
        verbose_name='Title',
    )
    number_in_seq = models.PositiveIntegerField(
        verbose_name='Number in sequence',
    )
