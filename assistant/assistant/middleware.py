from django.utils import translation

class SetLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.GET.get('lang')
        if lang:
            translation.activate(lang)
            request.LANGUAGE_CODE = translation.get_language()
        response = self.get_response(request)
        return response
