from django.shortcuts import redirect
from django.urls import reverse

class RestrictDirectAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        allowed_views = ['index', 'unauthorized_access_page']

        if request.path.startswith('/admin/'):
            return None  

        resolver_match = request.resolver_match
        if resolver_match:
            current_view_name = resolver_match.view_name
        else:
            current_view_name = None

        if current_view_name in allowed_views:
            return None

        referer = request.META.get('HTTP_REFERER')
        if not referer:
            return redirect(reverse('unauthorized_access_page'))

        return None