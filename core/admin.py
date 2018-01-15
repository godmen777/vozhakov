from django.contrib import admin
from core.models import VideoCategory, Video, SiteConfig, SiteMenu, SiteMenuItem, Page, Article, News, Review, Question, Direction


class SiteConfigAdmin(admin.ModelAdmin):
    model = SiteConfig


class SiteMenuItemAdmin(admin.ModelAdmin):
    model = SiteMenuItem
    ordering = ('weight',)
    list_display = ('name', 'url', 'weight')
    list_filter = ('menu__name', )


class PageAdmin(admin.ModelAdmin):
    model = Page
    prepopulated_fields = {'slug': ('title',)}


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    prepopulated_fields = {'slug': ('title',)}


class NewsAdmin(admin.ModelAdmin):
    model = News
    prepopulated_fields = {'slug': ('title',)}


class DirectionAdmin(admin.ModelAdmin):
    model = Direction
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(SiteConfig, SiteConfigAdmin)
admin.site.register(SiteMenu)
admin.site.register(SiteMenuItem, SiteMenuItemAdmin)
admin.site.register(VideoCategory)
admin.site.register(Video)
admin.site.register(Page, PageAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Review)
admin.site.register(Question)
admin.site.register(Direction, DirectionAdmin)
