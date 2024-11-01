from django.db import models

class Team(models.Model):
    member_count = models.CharField(max_length=100)

class Profile(models.Model):
    PARTICIPATION_CHOICES = [
        ('frontend', '프론트엔드'),
        ('backend', '백엔드'),
        ('planning', '기획'),
        ('design', '디자인'),
    ]
    user_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    mbti = models.CharField(max_length=4)
    affiliations = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    participation_field = models.CharField(
        max_length=20,
        choices=PARTICIPATION_CHOICES
    )

    def __str__(self):
        return self.user_name