# Generated by Django 4.1.1 on 2022-10-07 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstyear', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WGrammar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=55)),
                ('lfile', models.FileField(upload_to='GMA/WGrammer')),
            ],
        ),
    ]
