from django.shortcuts import render
from core.models import Video, Page, Direction, Question, Review
from django.shortcuts import get_object_or_404


def index_view(request):
    video_list = Video.objects.all()
    first_page = None
    second_page = None
    error_message = None
    directions = None
    questions = None
    reviews = None
    try:
        first_page = Page.objects.get(is_main_first=True)
    except Exception:
        error_message = "Страница не добавлена в info блок"
    try:
        second_page = Page.objects.get(is_main_second=True)
    except Exception:
        error_message = "Страница не добавлена в info блок"
    try:
        directions = Direction.objects.all()
        for direction in directions:
            direction.page = Page.objects.get(direction=direction)
    except Exception:
        error_message = "Не смог получить cстраницу для direction (направления)"
    try:
        questions = Question.objects.all()[:2]
    except Exception:
        error_message = "Вопросы не удалось получить из базы"
    try:
        reviews = Review.objects.all()[:3]
    except Exception:
        error_message = "Отзывы не удалось получить из базы"
    
    print("error_message: {}".format(error_message))

    return render(request, "core/home.html", {
        'name': 'Home page',
        'video_list': video_list,
        'first_page': first_page,
        'second_page': second_page,
        'directions': directions,
        'questions': questions,
        'reviews': reviews,
        'error_message': error_message,
    })


def page_view(request, slug):
    page = get_object_or_404(Page, slug=slug)

    return render(request, "core/home.html", {
        'page': page,
    })