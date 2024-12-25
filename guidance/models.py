from django.db import models


from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()
    interests = models.TextField()
    education = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Career(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    required_skills = models.TextField()
