from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50,unique=True)
    post_info = models.TextField()
    slug = models.SlugField(max_length=50,unique=True,default=None)
    date = models.DateTimeField(default=None)
    url_field = models.URLField(blank=False,default=None)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

