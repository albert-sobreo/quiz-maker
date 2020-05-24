from django.db import models

# Create your models here.

qTypes = ['Multiple Choice', 'True or False']

class Quiz_Choices(models.Model):
    choice = models.CharField(max_length=1024)

    class Meta:
        db_table = 'quiz_choices'

    def __str__(self):
        return self.choice


class Quiz_Answer(models.Model):
    quiz_answer = models.ForeignKey(Quiz_Choices, on_delete=models.CASCADE)

    class Meta:
        db_table = "quiz_answer"

    def __str__(self):
        return str(self.quiz_answer)


class Quiz_Question(models.Model):
    question = models.CharField(max_length=1024)
    quiz_choices = models.ManyToManyField(Quiz_Choices, blank=True)
    quiz_answer = models.ForeignKey(Quiz_Answer, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = "quiz_question"

    def __str__(self):
        return self.question


class Quiz_Section(models.Model):
    quiz_type = models.CharField(max_length=255, null=True)
    instruction = models.CharField(max_length=512, null=True, blank=True)
    points_per_item = models.IntegerField(null=True)
    quiz_question = models.ManyToManyField(Quiz_Question, blank=True)

    class Meta:
        db_table = "quiz_section"

    def __str__(self):
        return "Section " + str(self.pk)


class Quiz_Event(models.Model):
    quiz_name = models.CharField(max_length=255)
    date = models.DateTimeField(null=True)
    deadline = models.DateTimeField()
    quiz_section = models.ManyToManyField(Quiz_Section, blank=True)

    class Meta:
        db_table = 'quiz_event'

    def __str__(self):
        return self.quiz_name


