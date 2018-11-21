from django.urls import path, re_path
from . import views

from accounts.views import (login_view, register_view, logut_view)
from emorecog.views import upload_sample

app_name = 'website'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'^tab/(?P<pk>[1])/', views.ProjectsOverview.as_view(), name='projects_overview'),
    path('tab/<int:pk>/', views.TabDetail.as_view(), name='tab_detail'),
    path('article/<int:pk>/', views.ArticleDetail.as_view(), name='article_detail'),
    #path('upload_sample/', upload_sample, name='upload_sample'),
    path('login/', login_view, name='login'),
    path('logout/', logut_view, name='logout'),
    path('register/', register_view, name='register'),
]