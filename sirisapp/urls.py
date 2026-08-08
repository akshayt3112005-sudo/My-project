from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('About/',views.About,name='About'),
    path('service/',views.service,name='service'),
    
]    
