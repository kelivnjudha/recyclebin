from django.db import models
from django.contrib.auth.models import User
from .images_utils import resize_image
from PIL import Image
# Create your models here.
class Upload(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Uploads'  # Changed verbose name to plural form

    def __str__(self):
        return self.name

class Info(models.Model):  # Changed model name to 'Info' with an uppercase 'I'
    upload = models.ForeignKey(Upload, related_name='uploaded_info', on_delete=models.CASCADE)
    Title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=False)
    reason_of_rejection = models.TextField(blank=True, null=False)
    Contact = models.CharField(max_length=225, default='N/A')
    image = models.ImageField(upload_to='upload_images', blank=True, null=False)  # Fixed field name 'imgae'
    likes = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(User, related_name='uploaded_info', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.

        # Open the uploaded image
        img = Image.open(self.image.path)
        target_height = 600
        img_resized = resize_image(img, target_height)
        img_resized.save(self.image.path)
