# Generated by Django 4.1.3 on 2022-12-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='course/course_video'),
        ),
    ]
