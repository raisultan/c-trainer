from django.db import models


class SequenceOption(models.Model):
    question = models.ForeignKey(
        to='exam.Sequence',
        on_delete=models.CASCADE,
        related_name='options',
        verbose_name='Вопрос',
    )
    title = models.CharField(
        max_length=214,
        verbose_name='Текст варианта ответа',
    )
    number_in_seq = models.PositiveIntegerField(
        verbose_name='Номер в последовательности',
    )

    def __str__(self):
        return f'Вариант ответа для {self.question.base_question.title}'
