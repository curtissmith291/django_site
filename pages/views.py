from django.http import HttpResponse
from django.shortcuts import render
from .forms import SquareForm

# Create your views here.

# Homepage
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

# scratch page for testing
def scratch_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "scratch.html", {})

def about_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "about.html", {})

def projects_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "projects.html", {})

# def square_view(request):
#     context = {}
#     context['form'] = SquareForm()
#     return render(request, "square.html", context)

def square_view(request):
    if request.method =="POST":
        input = request.POST.get('number')
        number = int(input)
        print(type(number))
        if type(number) == int:
            return HttpResponse(number**2)

    return render(request, "square.html")


def hello_form(request):
    if request.method == "POST":
        user = request.POST.get('username')
        last = request.POST.get('lastname')
        print(user)
        if type(user) == str:
            return HttpResponse(f'Hello {user} {last}, thanks for visiting my website :)')

    return render(request, "hello.html")