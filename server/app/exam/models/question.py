from django.db import models


class Question(models.Model):
    exam = models.ForeignKey(
        to='exam.Exam',
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Exam',
    )
    title = models.CharField(
        max_length=214,
        verbose_name='Title',
    )
    is_sequence = models.BooleanField(
        default=False,
        verbose_name='Is sequence',
    )
