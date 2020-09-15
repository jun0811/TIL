from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # image = models.ImageField(blank = True, upload_to = '%Y/%m/%d/')
    image = ProcessedImageField(
        blank = True,
        format = 'JPEG',
        processors = [Thumbnail(200,300)],
        options = {'quality': 90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)