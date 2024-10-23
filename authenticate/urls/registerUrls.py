from django.urls import path
from authenticate.views.registerView import register
urlpatterns = [
    path("register/", register, name='register'),
]