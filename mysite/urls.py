"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from fen.views import create_item_form, create_item
# from fen.views import create_item

urlpatterns = [
    path("fen/", include("fen.urls")),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    # path('create-form/', create_item, name="create-item"),
    # path("<pk>/", create_item, name="create-item"),
    # path("htmx/create-item-form/", create_item_form, name="create-item-form")
]
