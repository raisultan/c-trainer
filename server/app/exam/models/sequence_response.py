from django.db import models


class SequenceResponse(models.Model):
    base_question = models.ManyToManyField(
        to='exam.Sequence',
        related_name='responses',
        verbose_name='Вопрос',
    )
    user_exam = models.OneToOneField(
        to='exam.UserExam',
        on_delete=models.CASCADE,
        related_name='sequences',
        verbose_name='Экзамен пользователя',
    )
    title = models.CharField(
        max_length=214,
        verbose_name='Текст варианта ответа',
    )
    number_in_seq = models.PositiveIntegerField(
        verbose_name='Номер в последовательности',
    )

    def __str__(self):
        return f'Ответ пользователя для {self.base_question.base_question.title} - {self.title}'
