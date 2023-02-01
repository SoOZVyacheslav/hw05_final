from functools import wraps

from django.core.paginator import Paginator
from django.utils.decorators import available_attrs
from django.views.decorators.cache import cache_page

sort = 10  # Сортировка кол-ва записей


def paginator(post_list, request):
    paginator = Paginator(post_list, sort)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def cache_on_auth(timeout):
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            result = cache_page(
                timeout,
                key_prefix=(f"_auth_{request.user.is_authenticated}_"))
            return result(view_func)(request, *args, **kwargs)
        return _wrapped_view
    return decorator
