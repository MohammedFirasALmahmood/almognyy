# Generated by Django 4.1.1 on 2022-10-17 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_fname',
            new_name='student_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_lname',
        ),
    ]