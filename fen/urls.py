from django.urls import path

from . import views

app_name = "fen"
urlpatterns = [
    path("", views.index, name="index"),
    path('create-form/', views.create_item, name="create-item"),
]
