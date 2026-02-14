from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import random

def generate_uid():
    return random.randint(10000000, 99999999)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_data')
    img = models.ImageField(upload_to='profile_image/', null=True, blank=True)
    uid = models.IntegerField(unique=True, editable=False, default=generate_uid)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.uid}"
    
@receiver(post_save, sender=User)
def creat_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile_data'):
        instance.profile_data.save()