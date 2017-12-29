from django.contrib import admin
from config.models import SiteConfig


class SiteConfigAdmin(admin.ModelAdmin):
    model = SiteConfig


admin.site.register(SiteConfig, SiteConfigAdmin)
