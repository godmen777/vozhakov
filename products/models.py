from django.db import models
from image_cropping import ImageRatioField
from config.models import SiteConfig
from image_cropping.utils import get_backend


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

    def __init__(self, *args, **kwargs):
        super(ProductImage, self).__init__(*args, **kwargs)

    def get_url(self):
        return "/media/{}".format(self.image)

    def get_url_255x170(self):
        return get_backend().get_thumbnail_url(
            self.image,
            {
                'size': (255, 170),
                'box': self.cropping_255x170,
                'crop': True,
                'detail': True,
            }
        )

    def __str__(self):
        return self.product.__str__()

    def __unicode__(self):
        return self.product.__str__()