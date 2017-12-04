from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    description = models.CharField(max_length=250, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(Category, blank=True)
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    description = models.CharField(max_length=250, null=True, blank=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
