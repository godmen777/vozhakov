from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class VideoCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория видео"
        verbose_name_plural = "Категории видео"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    v_category = models.ForeignKey(VideoCategory, verbose_name="Выбрать категорию", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название видео")
    description = RichTextUploadingField(verbose_name="Описание видео", blank=True, null=True)

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name