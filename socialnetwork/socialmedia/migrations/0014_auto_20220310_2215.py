# Generated by Django 3.0.3 on 2022-03-10 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0013_auto_20220310_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='chats',
        ),
        migrations.AddField(
            model_name='useruserfriend',
            name='chat',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='UserUserChat',
        ),
    ]