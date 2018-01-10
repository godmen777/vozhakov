# -*- coding: utf-8 -*-
from core.models import SiteConfig
from django.contrib.sites.models import Site


def get_site_config(request):
    try:
        return SiteConfig.objects.get(site__domain=request.get_host())
    except Exception:
        return SiteConfig.objects.get_or_create(name=request.get_host(), site=Site.objects.get(id=1))[0]
