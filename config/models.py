from django.db import models
from django.contrib.sites.models import Site


class SiteConfig(models.Model):
    site = models.OneToOneField(Site, related_name="site", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название настройки", max_length=250)
    top_menu = models.OneToOneField("SiteMenu", verbose_name="Верхнее меню", on_delete=models.CASCADE)

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