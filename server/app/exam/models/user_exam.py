from django.db import models


class UserExam(models.Model):
    user = models.ForeignKey(
        to='users.BaseUser',
        on_delete=models.CASCADE,
        related_name='exams',
        verbose_name='Пользователь',
    )
    base_exam = models.ForeignKey(
        to='exam.Exam',
        on_delete=models.CASCADE,
        related_name='user_exams',
        verbose_name='Экзамен',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    time_spent = models.PositiveIntegerField(
        verbose_name='Потраченное время',
    )

    def __str__(self):
        return f'{self.created_at} - {self.user.get_full_name()} - {self.base_exam.title}'
