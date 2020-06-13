from django.contrib import admin

from exam.models import (
    Choice, ChoiceOption, ChoiceResponse, Exam, Question, Sequence, SequenceOption,
    SequenceResponse, UserExam,
)

admin.site.register((
    Choice, ChoiceOption, ChoiceResponse, Exam, Question, Sequence, SequenceOption,
    SequenceResponse, UserExam,
))
