from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<str:item>", views.item, name = "item_page"),
    path("<str:item>/place_bid",views.place_bid, name="place_bid"),
]
