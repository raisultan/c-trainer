from django.db import models


class Question(models.Model):
    exam = models.ForeignKey(
        to='exam.Exam',
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Экзамен',
    )
    title = models.CharField(
        max_length=214,
        verbose_name='Заголовок вопроса',
    )
    is_sequence = models.BooleanField(
        default=False,
        verbose_name='Последовательность',
    )

    def __str__(self):
        return self.title
