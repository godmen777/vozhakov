from django.contrib import admin
from products.models import Product, Category, ProductImage
# from image_cropping import ImageCroppingMixin


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('name', ), }


# class ProductImageAdmin(ImageCroppingMixin, admin.StackedInline):
#     model = ProductImage
#     extra = 1
#
#
# class ProductAdmin(admin.ModelAdmin):
#     model = Product
#     prepopulated_fields = {'slug': ('name', ), }
#     inlines = [
#         ProductImageAdmin,
#     ]


admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductImage, ProductImageAdmin)
