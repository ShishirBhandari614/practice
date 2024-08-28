from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import *
# Create your views here.


def get_form_data():
    return FormName.objects.all()


def index(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        image = request.FILES.get("image")
        FormName.objects.create(name=name, email=email, password=password, image=image)
        return redirect('/signup/')

    # query = FormName.objects.all()
    # context= {'form':query}
    return render(request, "index.html")


def template_engine(request):
    peoples=[
        {'name':'shishir','age':21},
        {'name': 'samyush', 'age': 23},
        {'name': 'sagar', 'age': 19},
        {'name': 'sachin', 'age': 22}
    ]

    return render(request, "templating.html", context={'peoples':peoples})


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def view(request):
    query = get_form_data()
    context = {'form': query}
    return render(request, "view.html", context)


def delete_data(request, id):
    query = FormName.objects.get(id=id)
    query.delete()
    return redirect("/view/")


def update_data(request, id):
    query = FormName.objects.get(id=id)
    #query.update()
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        image = request.FILES.get("image")
        query.name=name
        query.email=email
        query.password=password
        if image:
            query.image=image
        query.save()
    context = {'form': query}
    return render(request, "update.html", context)


def update(request):
    return redirect(request,"update.html")
