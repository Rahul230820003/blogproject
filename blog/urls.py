from django.urls import path
from . import views
from .views import view_all_blogs

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_blog, name='create_blog'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('blogs/', view_all_blogs, name='view_blogs'),
]
