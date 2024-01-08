from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:book_id>',views.show ,name="show"),
    path("/about", views.aboutPage, name="aboutPage"),
    path("/contact", views.contactPage, name="contactPage"),

]