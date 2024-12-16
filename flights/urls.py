from django.urls import path,include

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<int:flight_id>",views.flight,name="flight"),
    path("book/<int:flight_id>/book",views.book,name="book"),
    path("users/",include("users.urls"))
]
