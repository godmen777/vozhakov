from django.contrib import admin
from products.models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
	model = Category
	prepopulated_fields = {'slug': ('name', ), }


class ProductAdmin(admin.ModelAdmin):
	model = Product
	prepopulated_fields = {'slug': ('name', ), }


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
