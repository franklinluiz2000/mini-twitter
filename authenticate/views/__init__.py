from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .homeView import *
from .authView import *
from .profileView import *
from .userView import *
from .searchView import *

