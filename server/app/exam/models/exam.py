from django.db import models


class Exam(models.Model):
    title = models.CharField(
        max_length=214,
        verbose_name='Заголовок экзамена',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    max_time = models.PositiveIntegerField(
        verbose_name='Максимальное кол-во времени для экзамене (секунды)',
    )

    @property
    def questions_count(self):
        return self.questions.count()

    def __str__(self):
        return self.title
