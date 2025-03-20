from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('post/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.blog_create, name='blog_create'),
    path('update/<int:pk>/', views.blog_update, name='blog_update'),
    path('delete/<int:pk>/', views.blog_delete, name='blog_delete'),
    # API URLs
    path('api/posts/', views.BlogPostListCreateAPIView.as_view(), name='api_post_list_create'),
    path('api/posts/<int:pk>/', views.BlogPostRetrieveUpdateDestroyAPIView.as_view(), name='api_post_detail'),
    path('api/comments/', views.CommentListCreateAPIView.as_view(), name='api_comment_list_create'),
]