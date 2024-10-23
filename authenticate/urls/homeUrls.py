from django.urls import path
from authenticate.views.homeView import home_view

urlpatterns = [
    path("", home_view),
]