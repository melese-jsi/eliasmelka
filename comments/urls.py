from django.urls import path

from comments.views import postComment

urlpatterns=[
    path('post_comment/<int:music_id>',postComment,name='post_comment')
]