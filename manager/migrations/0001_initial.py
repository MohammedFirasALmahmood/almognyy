# Generated by Django 4.1.1 on 2022-10-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_fname', models.CharField(max_length=500)),
                ('student_lname', models.CharField(max_length=500)),
                ('student_Phone', models.CharField(max_length=500, unique=True)),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=20)),
                ('student_balance', models.IntegerField(default=0)),
            ],
        ),
    ]
