from django.urls import path
from authenticate.views.authView import login_view, register_view, recovery_view, logout_view

urlpatterns = [
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
    path('recovery', recovery_view, name='recovery'),  
    path('logout', logout_view, name='logout'),      
]