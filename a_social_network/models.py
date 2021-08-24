from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractUser):
#     pass

class Profile(models.Model):
    poster = models.ForeignKey('app_mail.User', on_delete=models.CASCADE, related_name='followers', default=0)
    follower = models.ForeignKey('app_mail.User', on_delete=models.CASCADE, related_name='posters')
 

class Name(models.Model):
    user = models.CharField(max_length=64)
    content = models.TextField(max_length=64)
    timestamp = models.CharField(max_length=64)
    likes = models.ManyToManyField('app_mail.User', default=None, blank=True, related_name='post_likes')
    following = models.ManyToManyField('app_mail.User', default=None, blank=True, related_name='following')
    @property
    def num_likes(self):
        return self.liked.all().count()
    def __str__(self):
        return str(self.following.count())
    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "content":self.content,
            "timestamp":self.timestamp,
            "likes":self.likes.count(),
        }
class Like(models.Model):
    user = models.ForeignKey('app_mail.User', on_delete=models.CASCADE)
    post = models.ForeignKey('Name', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.post)

class Follow(models.Model):
    user = models.ForeignKey('app_mail.User', on_delete=models.CASCADE)
    followed_user = models.ForeignKey('Name', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.followed_user)

