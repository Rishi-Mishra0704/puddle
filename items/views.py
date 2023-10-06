from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Item, Category
from .forms import ItemForm, EditItemForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'items/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def details(request, pk):
    item = Item.objects.get(pk=pk)
    related_item = Item.objects.filter(
        category=item.category).exclude(pk=pk)[:3]

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

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)  # Define the form here

    context = {"form": form}
    return render(request, "items/form.html", context)


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')
