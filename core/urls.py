from django.urls import path
from core.views import index_view, page_view


urlpatterns = [
    path('', index_view, name="home"),
    path(r'pages/<slug>/', page_view, name="page"),
]
