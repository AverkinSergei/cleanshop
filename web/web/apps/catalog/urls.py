from django.urls import path

from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.MainView.as_view(), name='main')
]
