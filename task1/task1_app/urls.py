from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('click', views.click, name='click'),
    path('form', views.form, name='form'),
    path('message', views.message, name='message'),

]