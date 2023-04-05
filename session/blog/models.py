from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    reported = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]