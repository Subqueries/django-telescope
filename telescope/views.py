import json
from django.shortcuts import render
from telescope.models import Entry
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    requests = Entry.objects.all()

    paginator = Paginator(requests, 10)
    page = request.GET.get("page", 1)
    search = request.GET.get("search", '')

    try:
        paginated_items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_items = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        paginated_items = paginator.page(paginator.num_pages)

    requests = [
        {
            'type': item.type,
            'created_at': item.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
            'content': json.loads(item.content),
        }
        for item in paginated_items
    ]

    return render(request, "requests/index.html", {'requests': json.dumps({'values': requests}), 'paginated_items': paginated_items, 'search': search})
