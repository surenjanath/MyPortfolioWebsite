# Generated by Django 3.2.7 on 2021-09-25 21:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('Name', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=200)),
                ('Message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects_item',
            fields=[
                ('Project', models.CharField(max_length=250)),
                ('Link', models.TextField()),
                ('Image', models.ImageField(upload_to='images/')),
                ('Summary', models.CharField(max_length=200)),
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Achievement',
            fields=[
                ('achievements', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Education',
            fields=[
                ('School', models.CharField(max_length=250)),
                ('Course', models.CharField(max_length=250)),
                ('Date', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Experience',
            fields=[
                ('Work', models.CharField(max_length=250)),
                ('Company', models.CharField(max_length=200)),
                ('Date', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Skill',
            fields=[
                ('skill', models.CharField(max_length=250)),
                ('progress', models.CharField(max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Udemy',
            fields=[
                ('course', models.CharField(max_length=250)),
                ('progress', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
