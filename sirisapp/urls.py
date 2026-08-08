from django.urls import path
from . import views
urlpatterns = [
    path('Home/',views.Home,name='Home'),
    path('About/',views.About,name='About'),
    path('service/',views.service,name='service'),
    
]    
