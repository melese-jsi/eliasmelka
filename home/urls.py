from django.urls import path

from .views import home, album_detail, recent_releases, popular_albums, community_songs, all_albums, interviews

urlpatterns=[
    path('',recent_releases,name='recent_releases'),
    path('recent_releases',recent_releases,name='recent_releases'),
    path('popular_albums',popular_albums,name='popular_albums'),
    path('community_songs',community_songs,name='community_songs'),
    path('interviews',interviews,name='interviews'),
    path('all_albums', all_albums, name='all_albums'),
    path('<int:album_id>',album_detail, name='album_detail')
]