from django.core.paginator import Paginator

def get_page(request, obj_list):
    """Пагинатор для страниц с выводом списка постов."""

    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj