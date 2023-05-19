from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
import random



from . import util
from .forms import NewEntry


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request , name):
    if util.get_entry(name) != None:
        page = util.get_entry(name)
        title = name
        
        return render(request,"encyclopedia/entry.html",{"page":page,"title":title})
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
                return render(request,"encyclopedia/entry.html",{"page": util.get_entry(title),"title":title})
        else:
            return render(request, "encyclopedia/new_page.html", {"form": form})



    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewEntry()

    return render(request, "encyclopedia/new_page.html", {"form": form})

def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        util.save_entry(title,content)
        return render(request, "encyclopedia/edit_page.html", {"title":title,"content": content})
def save_edit(request):
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            util.save_entry(title,content)
            page = util.get_entry(title)
        return render(request,"encyclopedia/entry.html",{"page":page,"title":title})
        

def random_page(request):
    random_entry = random.shuffle(util.list_entries())
    all_entries = util.list_entries()
    i = random.choice(all_entries)
    title = i    
    page = util.get_entry(i)
    return render(request,"encyclopedia/entry.html",{"page":page,"title":title})





    
    
        









