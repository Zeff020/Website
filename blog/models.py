from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    subtitle = models.TextField(null=True, blank = True)
    subheader1 = models.TextField(null=True, blank = True)
    subheader2 = models.TextField(null=True, blank = True)
    subheader3 = models.TextField(null=True, blank = True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pics', blank=True, null=True)
    image1 = models.ImageField(upload_to='post_pics', blank=True, null=True)
    image2 = models.ImageField(upload_to='post_pics', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name='images')
    image = models.ImageField(upload_to='postimage_pics')