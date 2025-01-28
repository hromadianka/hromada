from django.utils.translation import get_language

def current_language_processor(request):
    return {
        'current_language': get_language(),
    }
