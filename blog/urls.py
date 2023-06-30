from django.urls import path
from . import views
from users.views import register




urlpatterns = [
    path('',views.home,name='blog-home'), #name are just anotations, just to remember each route
    path('about/',views.about,name='blog-about'),
]
