from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True)
    is_artist = models.BooleanField(default=False)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_groups',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_permissions',
        related_query_name='customuser',
    )

    def __str__(self):
        return self.username

class Song(models.Model):
    title = models.CharField(max_length=200)
    duration = models.DurationField()
    audio_file = models.FileField(upload_to='songs/')
    upload_date = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=50, blank=True)
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True, blank=True)
    artist = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    likes = models.ManyToManyField(CustomUser, related_name='liked_songs', blank=True)

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    artist = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='album_covers/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class Playlist(models.Model):
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.song or self.album or self.playlist}"