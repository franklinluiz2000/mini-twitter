from django.urls import path
from authenticate.views.searchView import SearchView
urlpatterns = [
    path("", SearchView, name='search'),
]