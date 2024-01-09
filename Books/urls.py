from django.urls import path

from . import views
from Books.views import BookListView,BookDetailView

urlpatterns = [
    # path("", views.index, name="index"),
    path('',BookListView.as_view(),name="index"),
    path('<int:pk>',BookDetailView.as_view(),name="show"),
    # path('<int:book_id>',views.show ,name="show"),
    path("/about", views.aboutPage, name="aboutPage"),
    path("/contact", views.contactPage, name="contactPage"),

]