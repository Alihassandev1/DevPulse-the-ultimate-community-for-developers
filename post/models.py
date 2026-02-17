from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.crypto import get_random_string
from pgvector.django import VectorField

def post_id_creation():
    return get_random_string(length=12)

# Create your models here.
class Post(models.Model):
    id = models.CharField(max_length=12, primary_key=True, editable=False, default=post_id_creation)
    content = RichTextUploadingField(blank=True, null=True)
    embedding = VectorField(dimensions=384, null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return self.id

'''
?: (ckeditor.W001) django-ckeditor bundles CKEditor 4.22.1 which isn't supported anymore and which does have
 unfixed security issues, see for example https://ckeditor.com/cke4/release/CKEditor-4.24.0-LTS . You should
 consider strongly switching to a different editor (maybe CKEditor 5 respectively django-ckeditor-5 after 
 checking whether the CKEditor 5 license terms work for you) or switch to the non-free CKEditor 4 LTS package. 
 See https://ckeditor.com/ckeditor-4-support/ for more on this. (Note! This notice has been added by the 
 django-ckeditor developers and we are not affiliated with CKSource and were not involved in the licensing 
 change, so please refrain from complaining to us. Thanks.)
'''