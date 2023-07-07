from django.urls import path
from blog.views import home,about,PostListView,DetailedListView,PostCreateView,PostUpdateView
from users.views import register



urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'), #name are just anotations, just to remember each route
    path('post/<int:pk>/',DetailedListView.as_view(),name='post-detail'),
    path('about/',about,name='blog-about'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update')
]
