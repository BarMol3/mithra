# Generated by Django 3.2.12 on 2022-02-05 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('processes', '0002_initial'),
        ('targets', '0001_initial'),
        ('projects', '0001_initial'),
        ('tools', '0001_initial'),
        ('telegram_bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramchat',
            name='configuration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.configuration'),
        ),
        migrations.AddField(
            model_name='telegramchat',
            name='process',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='processes.process'),
        ),
        migrations.AddField(
            model_name='telegramchat',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.project'),
        ),
        migrations.AddField(
            model_name='telegramchat',
            name='target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='targets.target'),
        ),
        migrations.AddField(
            model_name='telegramchat',
            name='target_port',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='targets.targetport'),
        ),
        migrations.AddField(
            model_name='telegramchat',
            name='tool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.tool'),
        ),
    ]
