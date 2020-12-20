from django.urls import path

from .views import HerokuWebIndex

urlpatterns = [
    path('', HerokuWebIndex, name='index')
]
