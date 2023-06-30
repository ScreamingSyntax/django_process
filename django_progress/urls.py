from django.contrib import admin
from django.urls import path,include
from users.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/',include('playground.urls')),
    path('',include('blog.urls')),
    path('register/',register,name='register')
]
