# Generated by Django 4.1.1 on 2022-10-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_rename_student_phone_student_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='activation_code',
            field=models.IntegerField(default=0),
        ),
    ]