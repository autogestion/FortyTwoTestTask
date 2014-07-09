from django.conf import settings

def load_settings(request):
    return {'settings': settings}
