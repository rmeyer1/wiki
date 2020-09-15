from functools import reduce

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from . import util

import operator

from django.db.models import Q


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


def entry(request, title):
    entries = util.list_entries()

    if title in entries:
        content = util.get_entry(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })
    else:
        return render(request, "encyclopedia/entry.html")




def mysearch(request):
    """This view builds a Q object query based on which fields are filled."""
    if 'submit' in request.POST:
        # build Q object depending on fields submitted
        q = Q()
        if request.POST['first_field']:
            q &= Q(firstfield__icontains = request.POST['first_field'])

        ...

        if request.POST['sixth_field']:
            q &= Q(sixthfield__icontains = request.POST['sixth_field'])

        results_list = MyModel.objects.filter(q)
        count = len(results_list)

        # store results
        request.session['results_list'] = results_list
        request.session['count'] = count

    # 'p' is an arbitrary marker to detonate pagination of a page other than 1
    if 'p' in request.GET:
        results_list = request.session['results_list']
        count = request.session['count']

    if count and count > 0:
        ...
        # pagination code
        ...

    else:
        pass
    return render_to_response('search_results.html',
        locals(), context_instance=RequestContext(request))