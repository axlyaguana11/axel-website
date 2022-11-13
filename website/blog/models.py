from django.db import models
from django.utils import timezone
import datetime 

PUBLISHED = (
    (False, 'Draft'),
    (True, 'Published')
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(choices=PUBLISHED, default=False)

    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return self.title