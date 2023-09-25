from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Upload(models.Model):
    image = models.ImageField(upload_to='Upload_images', blank=True, null=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    reason_of_rejection = models.TextField(blank=True, null=False)
    #created_by = models.ForeignKey(User, related_name='Upload', on_delete=models.CASCADE, null=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Upload'
        
    def __str__(self):
        return self.name
