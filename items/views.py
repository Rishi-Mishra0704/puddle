from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from .forms import ItemForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def details(request, pk):
    item = Item.objects.get(pk=pk)
    related_item = Item.objects.filter(category=item.category).exclude(pk=pk)[:3]

    context = {"item": item, "related_item": related_item}
    return render(request, "items/details.html", context)


@login_required
def new_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('detail', pk=item.id)
        else:
            form = ItemForm()
    context = {"form": form}
    return render(request, "items/new_item.html", context)