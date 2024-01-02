from django.shortcuts import render

from telescope.models import Entry


def index(request):
    # requests = Entry.objects.all()
    requests = [{}, {}, {}]
    return render(request, "requests/index.html", {'requests': requests})
