# Generated by Django 4.1.1 on 2022-10-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstyear', '0010_agrammer4_alter_wgmaglden_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AGrammer1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=55)),
                ('lfile', models.FileField(upload_to='GMA/WMorphology')),
                ('lprice', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'نحو 1 اتمتة',
            },
        ),
    ]
