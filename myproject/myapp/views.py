from typing import Dict

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
#from .forms import LogForm


# Create your views here.
def home(request):
    path = request.path
    scheme = request.scheme
    path_info = request.path_info
    method = request.method
    user_agent = request.META["HTTP_USER_AGENT"]

    response = HttpResponse()
    response.headers['Age'] = 20

    msg = f"""<br>
    <br> Path: {path}
    <br> Scheme: {scheme}
    <br> Path info: {path_info}
    <br> Method: {method}
    <br> User agent: {user_agent}
    <br> Response header: {response.headers}
    """

    return HttpResponse(msg, content_type='text/html', charset='utf-8')


def menu(request):
    new_menu = {'mains':[
        {'name': 'Greek Salad', 'price': 10},
        {'name': 'Pasta', 'price': 15},
        {'name': 'Pizza', 'price': 20},
        {'name': 'Burger', 'price': 25},
        {'name': 'Noodles', 'price': 30},
    ]
    }
    return render(request, 'menu.html', new_menu)


def display_date(request):
    return HttpResponse(datetime.today())


def dishes_with_path(request, dish):
    items = {
        "pasta": "Pasta is an italian dish",
        "noodles": "Noodles is a chinese dish"
    }
    return HttpResponse(f"<h2> {dish} </h2>" + items[dish])


def dishes_with_query(request):
    dish = request.GET['dish']
    items = {
        "pasta": "Pasta is an italian dish",
        "noodles": "Noodles is a chinese dish"
    }

    return HttpResponse(f"<h2> {dish} </h2>" + items[dish])


def regex(request):
    ...


def form_view(request):
    form = LogForm()
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "home.html", context=context)


def about(request):
    about_context = {"about": "Little Lemon is restaurant with good hill-side views"}
    return render(request, "about.html", about_context)
