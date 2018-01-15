from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.sites.models import Site


class SiteConfig(models.Model):
    site = models.OneToOneField(Site, related_name="site", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название настройки", max_length=250)
    top_menu = models.OneToOneField("SiteMenu",
                                    verbose_name="Верхнее меню",
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank=True)

    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class SiteMenu(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Меню сайта"
        verbose_name_plural = "Меню сайта"

    def get_menu_items(self):
        return SiteMenuItem.objects.filter(menu=self)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class SiteMenuItem(models.Model):
    parent = models.ForeignKey("self",
                                verbose_name="Родительский пункт",
                                on_delete=models.CASCADE,
                                blank=True, null=True)
    menu = models.ForeignKey(SiteMenu, verbose_name="Привязать к меню", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название пункта меню", max_length=255)
    url = models.CharField(verbose_name="URL пункта меню", max_length=255)
    weight = models.IntegerField(verbose_name="Вес пункта меню")

    class Meta:
        unique_together = ('menu', 'weight',)
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


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
    link = models.CharField(max_length=255, verbose_name="Ссылка на видео")
    description = RichTextUploadingField(verbose_name="Описание видео", blank=True, null=True)

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Direction(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название направления")
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to="directions", verbose_name="Изображение")

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"

    def get_image(self):
        return "/media/{}".format(self.image)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Page(models.Model):
    direction = models.ForeignKey(Direction, verbose_name="Направление", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="pages", blank=True, null=True)
    short_description = RichTextUploadingField(verbose_name="Краткое содержание")
    description = RichTextUploadingField(verbose_name="Содержание")
    is_main_first = models.BooleanField(default=False, verbose_name="Первый блок инфо на главной")
    is_main_second = models.BooleanField(default=False, verbose_name="Второй блок инфо на главной")

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def get_image(self):
        return "/media/{}".format(self.image)

    def get_url(self):
        return "/pages/{}".format(self.slug)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True)
    description = RichTextUploadingField(verbose_name="Содержание")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True)
    description = RichTextUploadingField(verbose_name="Содержание")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.CharField(max_length=255, verbose_name="email")
    text = models.TextField(verbose_name="Отзыв")
    image = models.ImageField(upload_to="reviews", verbose_name="Изображение")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def get_image(self):
        return "/media/{}".format(self.image)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.CharField(max_length=255, verbose_name="email")
    text = models.TextField(verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Request(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    slug = models.SlugField(max_length=255, unique=True)
    email = models.CharField(max_length=255, verbose_name="email")
    phone = models.CharField(max_length=255, verbose_name="phone")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

