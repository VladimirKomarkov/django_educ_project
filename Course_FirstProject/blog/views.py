from django.shortcuts import render


def index(request):
    header = "Данные пользвателя"
    langs = ["Python", "Java", "C#"]
    user = {"name": "Tom", "age": 23}
    address = ("Абрикосовая", 23, 45)
    data = {"header": header, "langs": langs, "user": user, "address": address}
    return render(request, "blog/index.html", context=data)

