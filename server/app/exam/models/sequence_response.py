from django.db import models


class SequenceResponse(models.Model):
    base_question = models.ForeignKey(
        to='exam.Sequence',
        on_delete=models.CASCADE,
        related_name='responses',
        verbose_name='Sequence Question',
    )
    user_exam = models.OneToOneField(
        to='exam.UserExam',
        on_delete=models.CASCADE,
        related_name='sequences',
        verbose_name='UserExam',
    )
    title = models.CharField(
        max_length=214,
        verbose_name='Title',
    )
    number_in_seq = models.PositiveIntegerField(
        verbose_name='Number in sequence',
    )
