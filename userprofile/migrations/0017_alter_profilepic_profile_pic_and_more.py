# Generated by Django 4.0.4 on 2022-06-02 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0016_alter_profilepic_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepic',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='profilepic',
            name='user_pic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_pic', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.CharField(max_length=100, null=True)),
                ('user_blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_blog_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
