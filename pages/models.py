from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    shorttext = models.CharField(max_length=150, null=True)
    text = RichTextUploadingField(null=True)
    date = models.DateField(null=True)
    time = models.DateTimeField(null=True, auto_now_add=True)
    img = models.ImageField(null=True)

    @property
    def get_image(self):
        try:
            return self.img.url
        except:
            return ""

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = RichTextUploadingField(null=True)
    time = models.DateTimeField(null=True, auto_now_add=True)
    img = models.ImageField(null=True)

    @property
    def get_image(self):
        try:
            return self.img.url
        except:
            return ""

    def __str__(self):
        return self.title
