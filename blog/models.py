from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Post(models.Model):
    title: models.CharField(max_length=200)
    text=models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.SET(get_sentinel_user),)
    created_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(auto_now=True)

   
    def __str__(self):
        return self.title
