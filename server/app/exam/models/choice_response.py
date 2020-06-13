from django.db import models


class ChoiceResponse(models.Model):
    base_question = models.ForeignKey(
        to='exam.Choice',
        on_delete=models.CASCADE,
        related_name='responses',
        verbose_name='Вопрос',
    )
    user_exam = models.OneToOneField(
        to='exam.UserExam',
        on_delete=models.CASCADE,
        related_name='choices',
        verbose_name='Экзамен пользователя',
    )
    answer_id = models.PositiveIntegerField(
        verbose_name='ID варианта ответа',
    )

    def __str__(self):
        return f'Ответ пользователя для {self.base_question.base_question.title}'
