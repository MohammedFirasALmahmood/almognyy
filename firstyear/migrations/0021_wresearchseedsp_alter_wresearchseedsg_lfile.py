# Generated by Django 4.1.1 on 2022-10-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstyear', '0020_wresearchseedsg_alter_wgrammar_lfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='WResearchSeedsP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=55)),
                ('lfile', models.FileField(upload_to='ResearchSeeds/P')),
                ('lprice', models.IntegerField(default=0)),
                ('number', models.IntegerField(default='1')),
            ],
            options={
                'verbose_name': 'اسئلة دورات اصول البحث',
                'ordering': ['number'],
            },
        ),
        migrations.AlterField(
            model_name='wresearchseedsg',
            name='lfile',
            field=models.FileField(upload_to='ResearchSeeds/G'),
        ),
    ]
