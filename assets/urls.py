from django.urls import path

from . import views

urlpatterns = [
    path('<asset_symbol>/', views.details, name='details'),
    path('', views.index, name='index')
]