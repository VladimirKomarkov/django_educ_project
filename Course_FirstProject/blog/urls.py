from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index),
    path("index/<int:id>/", views.index),
    path("access/<int:age>/", views.index),
    path("about/", views.about),
    path("contact/", views.contact),
    path("details/", views.details),
]
