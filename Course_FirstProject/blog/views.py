from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, \
    HttpResponseBadRequest, HttpResponseForbidden


def index(request, id):
    people = [None, "Bob", "Sam", "Tom"]
    if id in range(1, len(people)):
        return HttpResponse(people[id])
    else:
        return HttpResponseNotFound("Not Found")

def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("некорректные данные")
    if (age > 17):
        return HttpResponse("Доступ разрешен")
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")

def about(request):
    return HttpResponse('About')


def contact(request):
    return HttpResponseRedirect('/about')


def details(request):
    return HttpResponsePermanentRedirect('/')


def user(request):
    age = request.GET.get('age', 0)
    name = request.GET.get('name', 'Undefined')
    return HttpResponse(f"<h2>Имя: {name}, Возраст: {age}</h2>")


def products(request, id):
    return HttpResponse(f"Товар {id}")


def comments(request, id):
    return HttpResponse(f"Комментарий о товаре {id}")


def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")
