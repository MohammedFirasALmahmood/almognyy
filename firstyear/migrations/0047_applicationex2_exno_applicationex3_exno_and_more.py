# Generated by Django 4.1.1 on 2022-10-14 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstyear', '0046_applicationex1_exno'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationex2',
            name='ExNo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='firstyear.applicationexm'),
        ),
        migrations.AddField(
            model_name='applicationex3',
            name='ExNo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='firstyear.applicationexm'),
        ),
        migrations.AddField(
            model_name='applicationex4',
            name='ExNo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='firstyear.applicationexm'),
        ),
        migrations.AddField(
            model_name='applicationex5',
            name='ExNo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='firstyear.applicationexm'),
        ),
        migrations.AddField(
            model_name='applicationex6',
            name='ExNo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='firstyear.applicationexm'),
        ),
    ]
