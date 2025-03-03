from django.contrib import admin
from .models import CustomUser, Song, Album, Playlist, Comment

admin.site.register(CustomUser)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Playlist)
admin.site.register(Comment)