# Generated by Django 4.2.5 on 2023-09-29 06:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="workers",
            field=models.ManyToManyField(
                blank=True,
                related_name="task_and_workers",
                to="projects.worker",
                verbose_name="исполнитель задачи",
            ),
        ),
    ]
