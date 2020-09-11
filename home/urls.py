from django.urls import path

from .views import home, album_detail, recent_releases, popular_albums

urlpatterns=[
    path('',home,name='home'),
    path('recent_releases',recent_releases,name='recent_releases'),
    path('popular_albums',popular_albums,name='popular_albums'),
    path('<int:album_id>',album_detail, name='album_detail')
]