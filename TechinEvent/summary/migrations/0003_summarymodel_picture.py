# Generated by Django 2.2.13 on 2021-06-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0002_auto_20210628_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='summarymodel',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
