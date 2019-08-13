from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    slug = models.SlugField(blank=True, null=True)
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ('-post_date', )


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return 'علق {0} علي {1}'.format(self.name, self.post)

    class Meta:
        ordering = ('-comment_date', )