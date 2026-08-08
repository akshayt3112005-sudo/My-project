from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('About/',views.About,name='About'),
    path('service/',views.service,name='service'),
    path('navbar/',views.navbar,name='navbar'),
    path('traffic/',views.traffic,name='traffic'),
    path('contaner1/',views.contaner1,name='contaner1'),
    path('contaner2/',views.contaner2,name='contaner2'),
    path('contact/',views.contact,name='contact'),
    path('footer/', views.footer, name='footer'),
]    
