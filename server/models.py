from django.db import models


class Answer(models.Model):
    title = models.CharField(max_length=255)
    is_true = models.BooleanField()

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=255)
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.title


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title


class Result(models.Model):
    username = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return str(self.username)
