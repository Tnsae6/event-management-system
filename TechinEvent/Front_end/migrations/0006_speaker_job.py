# Generated by Django 2.2.13 on 2021-07-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front_end', '0005_speaker_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='job',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
    ]
