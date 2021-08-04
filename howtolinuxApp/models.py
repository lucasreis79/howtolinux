from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField()
    cover = models.ImageField(upload_to='imcovers/')
    distro = models.CharField(max_length=255)
    interface = models.CharField(max_length=255)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_post_url(self):
        return reverse('howtolinuxApp:detail', kwargs={'slug': self.slug})
