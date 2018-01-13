from django.shortcuts import render
from core.models import Video, Page
from django.shortcuts import get_object_or_404


def index_view(request):
    video_list = Video.objects.all()
    first_page = None
    second_page = None
    error_message = None
    try:
        first_page = Page.objects.get(is_main_first=True)
    except:
        error_message = "Страница не добавлена в info блок"
    try:
        second_page = get_object_or_404(Page, is_main_second=True)
    except:
        error_message = "Страница не добавлена в info блок"
    
    print("error_message: {}".format(error_message))

    return render(request, "core/home.html", {
        'name': 'Home page',
        'video_list': video_list,
        'first_page': first_page,
        'second_page': second_page,
        'error_message': error_message,
    })


def page_view(request, slug):
    page = get_object_or_404(Page, slug=slug)

    return render(request, "core/home.html", {
        'page': page,
    })