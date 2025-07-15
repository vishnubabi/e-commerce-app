from django.db import models

# models for theme
class SiteSetting(models.Model):
    banner= models.ImageField(upload_to='media/site/')
    caption=models.TextField()
