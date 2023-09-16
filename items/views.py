from django.shortcuts import render, get_object_or_404
from .models import Item, Category

# Create your views here.


def details(request, pk):
    item = Item.objects.get(pk=pk)
    related_item = Item.objects.filter(category=item.category).exclude(pk=pk)[:3]

    context = {"item": item, "related_item": related_item}
    return render(request, "items/details.html", context)
