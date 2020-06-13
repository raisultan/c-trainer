from django.db import models


class Sequence(models.Model):
    base_question = models.OneToOneField(
        to='exam.Question',
        on_delete=models.CASCADE,
        related_name='sequence',
        verbose_name='Базовый вопрос',
    )

    def __str__(self):
        return f'Последовательность: {self.base_question.title}'
