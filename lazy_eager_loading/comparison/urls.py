from django.urls import path
from . import views

urlpatterns = [
    path('lazy', views.index_lazy, name='index'),
    path('eager', views.index_eager, name='eager')
]
