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
    
def search(request):
    query = request.GET.get('q')
    if util.get_entry(query) != None:
        result = util.get_entry(query)
        return render(request,"encyclopedia/results.html",{"result":result})
    else:
       all_entries = util.list_entries()
       recommendations = []
       for entry in all_entries:
           if query.lower() in entry.lower():
               recommendations.append(entry)
       return render(request,"encyclopedia/recommended_entries.html",{"recommendations":recommendations,})
           





