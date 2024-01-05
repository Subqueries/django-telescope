import json
from django.shortcuts import render

from telescope.models import Entry


def index(request):
    requests = Entry.objects.all()

    requests = [
        {
            'type': item.type,
            'created_at': item.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
            'content': json.loads(item.content),
        }
        for item in requests
    ]

    return render(request, "requests/index.html", {'requests': json.dumps({'values': requests})})
