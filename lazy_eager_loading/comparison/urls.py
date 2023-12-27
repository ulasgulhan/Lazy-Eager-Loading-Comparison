from django.urls import path
from . import views

urlpatterns = [
    path('lazy/<int:id>', views.index_lazy, name='lazy'),
    path('lazy', views.index_lazy_all, name='lazy_all'),
    path('eager/<int:id>', views.index_eager, name='eager'),
    path('eager', views.index_eager_all, name='eager_all'),
    path('sql', views.index_eager_sql, name='eager_sql')
]
