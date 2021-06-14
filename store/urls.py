from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    path('logreg/', views.logreg, name="logreg"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('success/', views.success, name="success"),
    path('logout', views.logout, name="logout"),

    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact")
]