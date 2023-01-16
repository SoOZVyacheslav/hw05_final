from django.core.paginator import Paginator

sort = 10  # Сортировка кол-ва записей


def paginator(post_list, request):
    paginator = Paginator(post_list, sort)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'paginator': paginator,
        'page_number': page_number,
        'page_obj': page_obj,
    }
    return (context)
