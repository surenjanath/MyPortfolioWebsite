# Generated by Django 3.2.7 on 2021-09-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_resume_course_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects_item',
            name='Link',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='projects_item',
            name='Summary',
            field=models.TextField(),
        ),
    ]
