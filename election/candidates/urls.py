from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'candidates'
urlpatterns = [
    path('', views.index, name='index'),
    # path('candidates', views.list, name='list'),
    path('register', views.register, name='register'),
    # path('recommendations', views.recommendations, name='recommendations'),
    path('recommend', views.recommend, name='recommend'),
]
