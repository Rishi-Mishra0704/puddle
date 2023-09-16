from django.shortcuts import render, redirect
from items.models import Category, Item
from .forms import SignUpForm
# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[:6]
    categories = Category.objects.all()
    context = {
        "items": items,
        "categories": categories
    }
    return render(request, "core/index.html", context)


def contact(request):
    return render(request, "core/contact.html")


def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect("/login/")
        else:
            form = SignUpForm()
            print("invalid")
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "core/signup.html", context)