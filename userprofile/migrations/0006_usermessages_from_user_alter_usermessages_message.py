# Generated by Django 4.0.4 on 2022-05-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_alter_user_cardnumber_alter_user_cvc'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessages',
            name='from_user',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usermessages',
            name='message',
            field=models.CharField(max_length=500, null=True),
        ),
    ]