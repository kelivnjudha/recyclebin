from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Upload(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Upload'
        
    def __str__(self):
        return self.name

class info(models.Model):
    upload = models.ForeignKey(Upload, related_name='Upload', on_delete=models.CASCADE)
    Title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=False)
    reason_of_rejection = models.TextField(blank=True, null=False)
    Contact = models.CharField(max_length=225, default='N/A')
    imgae = models.ImageField(upload_to='upload_images', blank=True, null=False)
    created_by = models.ForeignKey(User, related_name='Upload', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Title