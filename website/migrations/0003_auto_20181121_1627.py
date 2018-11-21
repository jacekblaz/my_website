# Generated by Django 2.1.2 on 2018-11-21 15:27

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_audiosample_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audiosample',
            old_name='author',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='audiosample',
            name='audio_file',
            field=models.FileField(upload_to=website.models.user_directory_path),
        ),
    ]
