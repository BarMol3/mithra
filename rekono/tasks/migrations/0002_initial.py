# Generated by Django 3.2.10 on 2021-12-24 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tools', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('targets', '0001_initial'),
        ('processes', '0002_initial'),
        ('tasks', '0001_initial'),
        ('resources', '0002_wordlist_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='process',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='processes.process'),
        ),
        migrations.AddField(
            model_name='task',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='targets.target'),
        ),
        migrations.AddField(
            model_name='task',
            name='tool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.tool'),
        ),
        migrations.AddField(
            model_name='task',
            name='wordlists',
            field=models.ManyToManyField(blank=True, related_name='wordlists', to='resources.Wordlist'),
        ),
    ]
