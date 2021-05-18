from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [

    path("register/", user_views.register, name = "Register"),
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name = "Login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logout.html'), name = "Logout"),
    path("", views.index, name = "ShopHome"),
    path("about/", views.about, name = "ShopAbout"),
    path("crowns/", views.crowns, name = "ShopCrown"),
    path("masks/", views.masks, name = "ShopMask"),
    path("stones/", views.stones, name = "ShopStone"),
    path("suits/", views.suits, name = "ShopSuit"),
    path("weapons/", views.weapons, name = "ShopWeapon"),
    path("thanks", views.thanks, name = "ShopThank"),
]