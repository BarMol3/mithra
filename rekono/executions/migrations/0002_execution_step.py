# Generated by Django 3.2.11 on 2022-01-08 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('executions', '0001_initial'),
        ('processes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='execution',
            name='step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='processes.step'),
        ),
    ]
