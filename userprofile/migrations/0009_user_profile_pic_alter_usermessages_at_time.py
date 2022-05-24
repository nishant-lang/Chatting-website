# Generated by Django 4.0.4 on 2022-05-09 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_usermessages_at_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='usermessages',
            name='at_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
