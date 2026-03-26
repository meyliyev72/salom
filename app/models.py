from django.db import models
from django.utils.text import slugify

class Taom(models.Model):
    title = models.CharField(max_length=200) 
    ingredients = models.TextField()  
    instructions = models.TextField() 
    rasm = models.ImageField(upload_to="images/",default="css/images/salom.png",null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"