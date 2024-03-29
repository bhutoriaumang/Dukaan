from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("createlist", views.createlist, name="createlist"),
    path("login", views.login_view, name="login"),
    path("watch", views.watch, name="watch"),
    path("createwatch", views.createwatch, name="createwatch"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("item<str:item>", views.item, name = "item_page"),
    path("<str:item>/place_bid",views.place_bid, name="place_bid"),
]
