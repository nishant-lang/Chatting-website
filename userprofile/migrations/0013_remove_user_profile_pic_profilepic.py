# Generated by Django 4.0.4 on 2022-05-30 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_rename_chait_messages_chat_messages_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_pic',
        ),
        migrations.CreateModel(
            name='ProfilePic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='media')),
                ('user_pic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_pic', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
