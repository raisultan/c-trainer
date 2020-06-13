from django.db import models


class UserExam(models.Model):
    user = models.ForeignKey(
        to='users.BaseUser',
        on_delete=models.CASCADE,
        related_name='exams',
        verbose_name='User',
    )
    base_exam = models.ForeignKey(
        to='exam.Exam',
        on_delete=models.CASCADE,
        related_name='user_exams',
        verbose_name='User Exam',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    time_spent = models.PositiveIntegerField(
        verbose_name='Time spent',
    )
