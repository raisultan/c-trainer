from django.contrib.auth.models import AbstractUser
from django.db import models


class RoleChoices:
    TRAINER = 'trainer'
    STUDENT = 'student'
    ROLE_CHOICES = (
        (TRAINER, 'Тренер'),
        (STUDENT, 'Студент'),
    )


class BaseUser(AbstractUser):
    role = models.CharField(
        max_length=25,
        choices=RoleChoices.ROLE_CHOICES,
        default=RoleChoices.STUDENT,
        verbose_name='Role',
    )

    @property
    def is_trainer(self):
        return self.role == RoleChoices.TRAINER
