from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
        
class Country(models.Model):
    label = models.CharField(max_length=100)
    def __str__(self):
        return self.label

class Experience(models.Model):
    label = models.TextField(max_length=500)
    def __str__(self):
        return self.label


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    profile_picture = models.URLField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    job_title = models.CharField(max_length=100)
    experience = models.ForeignKey(Experience, on_delete=models.SET_NULL, blank=True, null=True)  # Changed "Experience" to "experience" to follow Python conventions
    website = models.URLField(max_length=200)
    description = models.TextField(max_length=1000)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()



class Interest(models.Model):
    label = models.TextField(max_length=400,blank=True,null=True)
class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Interest = models.ForeignKey(Interest,on_delete=models.CASCADE, blank=True, null=True)

