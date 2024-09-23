# Generated by Django 5.1 on 2024-09-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('demo_link', models.CharField(blank=True, max_length=500)),
                ('source_link', models.CharField(blank=True, max_length=500)),
                ('vote_total', models.IntegerField(default=0)),
                ('vote_ratio', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Заголовок',
                'verbose_name_plural': 'Заголовки',
            },
        ),
    ]