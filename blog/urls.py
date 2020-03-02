from django.urls import path
from .views import PostlistView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    path('', PostlistView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]

