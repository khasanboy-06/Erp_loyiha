# Generated by Django 5.0.6 on 2024-06-13 00:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('users', '0003_remove_student_teacher_team_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homework',
            name='homework_file',
            field=models.FileField(blank=True, null=True, upload_to='homeworks/'),
        ),
        migrations.AddField(
            model_name='homework',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='users.student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homework',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('homework_status', models.BooleanField(default=False)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='users.team')),
            ],
            options={
                'unique_together': {('team', 'title')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='homework',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='homework',
            name='lesson',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='homework', to='students.lesson'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='homework',
            unique_together={('student', 'lesson')},
        ),
        migrations.RemoveField(
            model_name='homework',
            name='team',
        ),
        migrations.RemoveField(
            model_name='homework',
            name='title',
        ),
        migrations.RemoveField(
            model_name='homework',
            name='update_time',
        ),
    ]
