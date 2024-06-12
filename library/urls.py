from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get/<slug:slug>',views.get, name="get-book"),
    path('books',views.getall, name="get-books"),
    path('update/<int:id>',views.update, name="update-book"),
    path('delete/<int:id>',views.delete, name="delete-book"),
    path('add/',views.add,name="add-book"),
]
