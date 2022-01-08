# Generated by Django 3.2.11 on 2022-01-08 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tools', '0001_initial'),
        ('inputs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_tool', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='output',
            name='configuration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outputs', to='tools.configuration'),
        ),
        migrations.AddField(
            model_name='output',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outputs', to='inputs.inputtype'),
        ),
        migrations.AddField(
            model_name='intensity',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intensities', to='tools.tool'),
        ),
        migrations.AddField(
            model_name='input',
            name='argument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='tools.argument'),
        ),
        migrations.AddField(
            model_name='input',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='inputs.inputtype'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configurations', to='tools.tool'),
        ),
        migrations.AddField(
            model_name='argument',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arguments', to='tools.tool'),
        ),
        migrations.AddConstraint(
            model_name='output',
            constraint=models.UniqueConstraint(fields=('configuration', 'type'), name='unique output'),
        ),
        migrations.AddConstraint(
            model_name='input',
            constraint=models.UniqueConstraint(fields=('argument', 'order'), name='unique input'),
        ),
        migrations.AddConstraint(
            model_name='configuration',
            constraint=models.UniqueConstraint(fields=('tool', 'name'), name='unique configuration'),
        ),
        migrations.AddConstraint(
            model_name='argument',
            constraint=models.UniqueConstraint(fields=('tool', 'name'), name='unique argument'),
        ),
    ]
