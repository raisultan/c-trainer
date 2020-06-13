from django.db import models


class ChoiceOption(models.Model):
    question = models.ForeignKey(
        to='exam.Choice',
        on_delete=models.CASCADE,
        related_name='options',
        verbose_name='Вопрос',
    )
    title = models.CharField(
        max_length=214,
        verbose_name='Текст варианта ответа',
    )
    is_correct = models.BooleanField(
        verbose_name='Правильный',
    )

    def __str__(self):
        return f'Вариант ответа для {self.question.base_question.title}'
