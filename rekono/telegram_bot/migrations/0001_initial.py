# Generated by Django 3.2.10 on 2021-12-24 12:20

from django.db import migrations, models
import telegram_bot.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField(unique=True)),
                ('start_token', models.TextField(max_length=200, unique=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('expiration', models.DateTimeField(default=telegram_bot.utils.get_token_expiration)),
            ],
        ),
    ]
