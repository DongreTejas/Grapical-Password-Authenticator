from django.urls import path, include
from .views import (
    home, 
    register_page, 
    login_page, 
    logout_page, 
    login_from_uid, 
    reset_view, 
    reset_from_uid,
    success,
    registersuccess,
    about,
    contact,
    )

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('login/<str:uid>', login_from_uid, name='login_uid'),
    path('logout/', logout_page, name='logout'),
    path('reset/', reset_view, name='reset'),
    path('reset/<str:uid>', reset_from_uid, name='reset_uid'),
    path('success', success, name='success'),
    path('resgistersuccess', registersuccess, name='registersuccess'),
    path('about',about, name='about'),
    path('contact',contact, name='contact'),

]
