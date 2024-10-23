from django.urls import path
from authenticate.views.userView import user_view
urlpatterns = [
    path("", user_view, name='users'),
    path("<int:id>", user_view, name='user'),
]