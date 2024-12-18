# Generated by Django 5.1.2 on 2024-11-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0007_profile_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="profile_images/"),
        ),
        migrations.AddField(
            model_name="team",
            name="team_name",
            field=models.CharField(default="team", max_length=50),
        ),
    ]
