from django.shortcuts import render
from core.models import Video


def index_view(request):
    video_list = Video.objects.all()

    return render(request, "core/home.html", {
        'name': 'Home page',
        'video_list': video_list,
    })
