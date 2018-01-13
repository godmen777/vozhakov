from django.shortcuts import render
from core.models import Video, Page
from django.shortcuts import get_object_or_404


def index_view(request):
    video_list = Video.objects.all()
    first_page = get_object_or_404(Page, is_main_first=True)
    second_page = get_object_or_404(Page, is_main_second=True)

    return render(request, "core/home.html", {
        'name': 'Home page',
        'video_list': video_list,
        'first_page': first_page,
        'second_page': second_page,
    })
