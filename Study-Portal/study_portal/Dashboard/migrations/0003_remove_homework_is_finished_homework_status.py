# Generated by Django 5.0.7 on 2024-08-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_homework'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='is_finished',
        ),
        migrations.AddField(
            model_name='homework',
            name='status',
            field=models.CharField(choices=[('not_started', 'Not Started'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='not_started', max_length=20),
        ),
    ]
