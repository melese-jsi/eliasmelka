from django.urls import path

from .views import home,album_detail

urlpatterns=[
    path('',home,name='home'),
    path('<int:album_id>',album_detail, name='album_detail')
]