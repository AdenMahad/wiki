from django.shortcuts import render
from django.http import HttpResponseNotFound



from . import util
from .forms import NewEntry


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
           

def create_entry(request):
    if request.method == "POST":
        form = NewEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title in util.list_entries():
                raise FileExistsError("file exists try another title name")
            else:
                util.save_entry(title,content)
                return render(request,"encyclopedia/new_entry.html",{"new_entry": util.get_entry(title)})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewEntry()

    return render(request, "encyclopedia/new_page.html", {"form": form})



