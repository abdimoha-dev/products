from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name= 'accounts'

urlpatterns=[
    path('signup', views.signup, name='signup'),
    path('login', auth_views.login,{'template_name': 'accounts/login.html'}, name='login'),
    path('logout', auth_views.logout, name='logout'),
]