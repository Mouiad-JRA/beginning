from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def homepage_view(requset, *args, **kwargs):
    # print(requset.user)
    return render(requset, "home.html", {})
    # return HttpResponse("<h1>hello world<h1>")


def contact_view(requset, *args, **kwargs):
    """
    :param requset:
    :param args:
    :param kwargs:
    :return:
    """
    return render(requset, "contact.html", {})


def about_view(requset, *args, **kwargs):
    my_context={
       "my":"this is about me",
        "number":123,
        "list":[1,2,3,4]
    }
    return render(requset, "about.html", my_context)


def social_view(requset, *args, **kwargs):
    return HttpResponse("<h1>social_view<h1>")
