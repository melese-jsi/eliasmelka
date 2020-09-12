from django.contrib import admin

from comments.models import Comment
from .models import Music, Interview


# Register your models here.
class commentAdmin(admin.TabularInline):
    model = Comment
class musicAdmin(admin.ModelAdmin):
    model=Music
    inlines = [commentAdmin]
admin.site.register(Music, musicAdmin)
admin.site.register(Comment)
admin.site.register(Interview)
