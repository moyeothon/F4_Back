from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    user_name = models.CharField(max_length=50) #유저네임 어떻게 가져올건데
    selected_option = models.CharField(max_length=1, choices=[('A', 'Option A'),('B', 'Option B')])

    def __str__(self):
        return f"{self.user_name} - {self.question} - {self.selected_option}"