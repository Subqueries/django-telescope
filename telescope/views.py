import json
from django.shortcuts import render
from telescope.models import Entry
from django.core.paginator import Paginator


def index(request):
    requests = Entry.objects.all()

    paginator = Paginator(requests, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    print(page_obj)

    requests = [
        {
            'type': item.type,
            'created_at': item.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
            'content': json.loads(item.content),
        }
        for item in requests
    ]

    return render(request, "requests/index.html", {'requests': json.dumps({'values': requests})})
