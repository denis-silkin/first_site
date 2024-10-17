from django.db import models
from django.core.validators import FileExtensionValidator


# модель для заполнения администратором сайта
class Administrator(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    # video = models.FileField(upload_to="documents/%Y/%m/%d", validators=['validate_file_extension'])
    video = models.URLField(max_length=500, null=True, blank=True, verbose_name='Видео')
    description = models.TextField(blank=True, verbose_name='Описание')
    demo_link = models.CharField(max_length=500, blank=True)
    source_link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'


# <iframe src="https://vk.com/video_ext.php?oid=115284178&id=456239464&hd=3" width="333" height="660"
#                     allow="autoplay; encrypted-media; fullscreen; picture-in-picture; screen-wake-lock;" frameborder="0"
#                     allowfullscreen></iframe>

# models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])