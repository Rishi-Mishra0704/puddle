from django.shortcuts import render, redirect
from items.models import Category, Item
from .models import Contact
from .forms import SignUpForm, ContactForm
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
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect("/")
        else:
            form = ContactForm()
            print("invalid")
            print(form.errors)
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