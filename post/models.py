from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.crypto import get_random_string

def post_id_creation():
    return get_random_string(length=12)

# Create your models here.
class Post(models.Model):
    id = models.CharField(max_length=12, primary_key=True, editable=False, default=post_id_creation)
    content = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to=f'post_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return self.id
