from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.urls import reverse

from authentication.models import User
from comments.models import Comment
from home.models import Music


def postComment(request,music_id):
    if request.method == 'POST':
        comment = request.POST['comment_body']
        music = get_object_or_404(Music,pk=music_id)
        print(request.user)
        if not comment =='' and request.user is not None:
            comment_obj= Comment(body=comment,author=User.objects.get(id=request.user.id),music=music)
            comment_obj.save()

    return HttpResponseRedirect(reverse('album_detail',args=(music_id,)))
