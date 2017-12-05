from django.db import models
from image_cropping import ImageRatioField


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

    def get_first_image(self):
        return ProductImage.objects.filter(product=self)[0]

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
    cropping_255x170 = ImageRatioField('image', '255x170')

    def get_url(self):
        return "/media/{}".format(self.image)

    def get_url_255x170(self):
        try:
            return "/media/{}".format(self.cropping_255x170)
        except Exception:
            return self.get_url()

    def __str__(self):
        return self.product.__str__()

    def __unicode__(self):
        return self.product.__str__()