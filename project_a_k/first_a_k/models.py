from django.db import models
from django.core.validators import FileExtensionValidator


# модель для заполнения администратором сайта
class Administrator(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    # image_video = models.FileField(upload_to='video/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
    #                          verbose_name='Видео')
    description = models.TextField(blank=True, verbose_name='Описание')
    demo_link = models.CharField(max_length=500, blank=True)
    source_link = models.CharField(max_length=500, blank=True)
    # tags = models.ManyToManyField()
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
