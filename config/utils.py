# -*- coding: utf-8 -*-
from config.models import SiteConfig


def get_site_config(request):
    try:
        return SiteConfig.objects.get(site__domain=request.get_host())
    except Exception:
        return SiteConfig.objects.get(id=1)
