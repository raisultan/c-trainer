from django.db import models


class Student(models.Model):
    user = models.OneToOneField(
        to='users.BaseUser',
        on_delete=models.CASCADE,
        related_name='student',
        verbose_name='Base User',
    )
