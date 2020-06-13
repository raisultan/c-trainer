from django.db import models


class ChoiceOption(models.Model):
    question = models.ForeignKey(
        to='exam.Choice',
        on_delete=models.CASCADE,
        related_name='options',
        verbose_name='Question',
    )
    title = models.CharField(
        max_length=214,
        verbose_name='Title',
    )
    is_correct = models.BooleanField(
        verbose_name='Is correct',
    )
