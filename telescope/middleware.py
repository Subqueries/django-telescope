import time
import json
from telescope.models import Entry
from telescope.watchers import RequestWatcher


class TelescopeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()

        Entry.objects.create(
            type=Entry.EntryTypes.REQUEST,
            content=json.dumps({
                'ip_address': request.META['REMOTE_ADDR'],
                'uri': request.get_full_path(),
                'method': request.method,
                # 'headers': request.META,
                # 'payload': request.META,
                # 'response': json.dumps(response),
                'response_status': response.status_code,
                'duration': end_time - start_time,
            }),
        )

        return response
