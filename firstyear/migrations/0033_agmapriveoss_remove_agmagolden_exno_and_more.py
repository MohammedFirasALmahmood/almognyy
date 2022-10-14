# Generated by Django 4.1.1 on 2022-10-10 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstyear', '0032_remove_wgmaglden_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='AGMAPriveosS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExNo', models.IntegerField(default=1)),
                ('semestery', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='agmagolden',
            name='ExNo',
        ),
        migrations.RemoveField(
            model_name='agmapriveos',
            name='ExNo',
        ),
        migrations.AddField(
            model_name='agmapriveos',
            name='PreviosS',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstyear.agmapriveoss'),
        ),
    ]
