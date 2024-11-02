# Generated by Django 5.1.2 on 2024-11-02 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0008_profile_profile_image_team_team_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="goals",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="team",
            name="rules",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="ProfileQuestionAnswer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "question_id",
                    models.IntegerField(
                        choices=[
                            (1, "이번 팀 프로젝트에서 가장 챙겨가고 싶은 점은 무엇인가요?"),
                            (2, "가장 중요하게 생각하는 협업 요소는 무엇인가요?"),
                            (3, "팀원들과의 관계에서 가장 중요하게 생각하는 점은 무엇인가요?"),
                            (4, "프로젝트가 끝난 후 팀원들에게 어떤 모습으로 기억되고 싶은가요?"),
                            (5, "프로젝트를 진행하면서 스스로에게 가장 엄격하게 적용하고 싶은 원칙은 무엇인가요?"),
                        ]
                    ),
                ),
                ("answer_id", models.IntegerField()),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="question_answers",
                        to="teams.profile",
                    ),
                ),
            ],
        ),
    ]
