from django.db import models


class SiteConfig(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
