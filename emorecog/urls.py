from django.urls import path
from . import views


app_name = 'emorecog'
urlpatterns = [
    path('upload_sample/', views.upload_sample, name='upload_sample'),
    path('my_samples/', views.my_samples, name='my_samples'),
]