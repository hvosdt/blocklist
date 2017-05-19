from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response, redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Item
from .forms import ItemForm


def index (request):
    return render_to_response("index.html")

def search (request):
    if "q" in request.GET:
            q = request.GET['q']
            listOfItems = Item.objects.filter(name__contains= q)
            return render_to_response("search_result.html", {'listOfItems' : listOfItems})

def fullList (request):
    listOfItems = Item.objects.order_by("pub_date")
    output = ", ".join([i.name for i in listOfItems])
    template = loader.get_template("fullList.html")
    context = {
        'listOfItems': listOfItems
    }
    return HttpResponse(template.render(context, request))

def add (request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.pub_date = timezone.now()
            item.save()
            return redirect('/add_result', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'add.html', {'form' : form})

def add_result(request):
    return render(request, 'add_result.html')