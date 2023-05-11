from django.shortcuts import render
from django.http import HttpResponseNotFound

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request , name):
    if util.get_entry(name) != None:
        page = util.get_entry(name)
        return render(request,"encyclopedia/entry.html",{"page":page,})
    else:
        return HttpResponseNotFound("<h1>Page not found</h1>")


