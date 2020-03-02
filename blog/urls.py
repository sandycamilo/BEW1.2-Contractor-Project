from django.urls import path
from .views import PostlistView, PostDetailView
from . import views

urlpatterns = [
    path('', PostlistView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
]

