from django.urls import path
from  . views import main,karakterler

urlpatterns = [
    path('',main,name='main'),
    path('alimler/<int:index>',karakterler,name='karakterler')
]
