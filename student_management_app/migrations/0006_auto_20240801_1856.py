# Generated by Django 3.0.7 on 2024-08-01 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0005_studentresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminhod',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='attendancereport',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='feedbackstaffs',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='feedbackstudent',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='leavereportstaff',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='leavereportstudent',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='notificationstaffs',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='notificationstudent',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='staffs',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='studentresult',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='students',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='students',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.Courses'),
        ),
    ]
