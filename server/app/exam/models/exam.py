from django.db import models


class Exam(models.Model):
    title = models.CharField(
        max_length=214,
        verbose_name='Title',
    )
    description = models.TextField(
        verbose_name='Description',
    )
    max_time = models.PositiveIntegerField(
        verbose_name='Max amount of time to spend',
    )

    @property
    def questions_count(self):
        return self.questions.count()
