# Generated by Django 4.0.4 on 2022-05-07 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_rename_from_user_usermessages_to_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessages',
            name='at_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]