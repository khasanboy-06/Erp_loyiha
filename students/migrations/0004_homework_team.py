# Generated by Django 5.0.6 on 2024-06-13 00:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_homework_homework_file'),
        ('users', '0003_remove_student_teacher_team_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homeworks', to='users.team'),
        ),
    ]
