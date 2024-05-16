from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('get_data/', views.get_data, name='get_data'),
    path('QueuePro/', views.Index, name='index'),
    path('registro/', views.Registro, name='registro'),
    path('ver/', views.Ver, name='ver'),
    path('logout/', views.logout_view, name='logout'),
]