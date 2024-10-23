from django.shortcuts import render, redirect
from authenticate.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .homeView import *
from .profileView import *
from .userView import *
