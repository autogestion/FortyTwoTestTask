from .models import HttpRequestList


class SaveAllHttpRequests(object):

    def process_request(self, request):
        HttpRequestList.objects.create(
            method=request.META['REQUEST_METHOD'],
            protocol=request.META['SERVER_PROTOCOL'],
            remote_addr=request.META.get('REMOTE_ADDR'),
            path_info=request.META['PATH_INFO']
        )
        return None
