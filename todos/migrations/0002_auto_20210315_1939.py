# Generated by Django 3.1.7 on 2021-03-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_Date',
        ),
        migrations.AddField(
            model_name='todo',
            name='todo_status',
            field=models.BooleanField(default=False),
        ),
    ]