from django.contrib import admin
from config.models import SiteConfig, SiteMenu, SiteMenuItem


class SiteConfigAdmin(admin.ModelAdmin):
    model = SiteConfig


class SiteMenuItemAdmin(admin.ModelAdmin):
    model = SiteMenuItem
    ordering = ('weight',)
    list_display = ('name', 'url', 'weight')
    list_filter = ('menu__name', )


admin.site.register(SiteConfig, SiteConfigAdmin)
admin.site.register(SiteMenu)
admin.site.register(SiteMenuItem, SiteMenuItemAdmin)
