from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField






class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_desc = models.TextField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    news_image = models.FileField(upload_to="news/", max_length=250, null=True, default=None)

    def save(self, *args, **kwargs):
        # Auto-generate slug if not provided
        if not self.slug:
            self.slug = slugify(self.news_title)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.news_title
