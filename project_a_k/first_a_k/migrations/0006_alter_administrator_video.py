# Generated by Django 5.1 on 2024-10-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_a_k', '0005_alter_administrator_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='video',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Видео'),
        ),
    ]