from django.urls import include, path
from .views import Translator


#URLS for Article APP
urlpatterns = [
    path('translator/', Translator , name='translator'),
]