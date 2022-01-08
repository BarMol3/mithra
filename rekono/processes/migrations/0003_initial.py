# Generated by Django 3.2.11 on 2022-01-08 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('processes', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_processes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='process',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_process', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='process',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddConstraint(
            model_name='step',
            constraint=models.UniqueConstraint(fields=('process', 'tool', 'configuration'), name='unique step'),
        ),
    ]
