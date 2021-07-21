from django.http import HttpResponse
from django.shortcuts import render
from .forms import SquareForm

# Create your views here.

# Homepage
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def home_view_2(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home_2.html", {})

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

def add_view(request):
    return render(request, 'add.html')    

def add_result_view(request):
    val1 = request.GET['num1']
    val2 = request.GET['num2']
    res = int(val1) + int(val2)
    return render(request, 'add_result.html', {'result': res})