from django.urls import path
from .views import demo, index

# url配置文件
urlpatterns = [
    path('demo/', demo, name='demo'),
    path('index/', index, name='index'),
]