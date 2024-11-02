# Generated by Django 5.1.2 on 2024-11-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0010_alter_profile_collaboration_environment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="communication_style",
            field=models.IntegerField(
                choices=[(1, "주기적 회의"), (2, "필요할 때만 연락")], default=1
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="editor_mode",
            field=models.IntegerField(choices=[(1, "라이트 모드"), (2, "다크 모드")], default=1),
        ),
        migrations.AlterField(
            model_name="profile",
            name="focus_time",
            field=models.IntegerField(choices=[(1, "아침"), (2, "야간")], default=1),
        ),
        migrations.AlterField(
            model_name="profile",
            name="preferred_os",
            field=models.IntegerField(
                choices=[(1, "Windows"), (2, "MacOS")], default=1
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="project_style",
            field=models.IntegerField(choices=[(1, "계획적"), (2, "즉흥적")], default=1),
        ),
        migrations.AlterField(
            model_name="profile",
            name="work_environment",
            field=models.IntegerField(
                choices=[(1, "조용한 환경"), (2, "시끌시끌한 카페")], default=1
            ),
        ),
    ]
