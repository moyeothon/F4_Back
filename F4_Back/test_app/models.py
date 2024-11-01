from django.db import models
from teams.models import Profile

#질문
class Test(models.Model):
    test_text = models.CharField(max_length=255)

    def __str__(self):
        return self.test_text

#선택지
class Choice(models.Model):
    test = models.ForeignKey(Test, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.test.test_text} - {self.choice_text}"

#질문에 대한 답
class TestAnswer(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.user_name} - {self.test.test_text} - {self.choice.choice_text}"