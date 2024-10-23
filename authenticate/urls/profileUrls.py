from django.urls import path
from authenticate.views.profileView import profile
urlpatterns = [
    path("", profile, name='profiles'),
    path("<int:id>", profile, name='profile'),
]