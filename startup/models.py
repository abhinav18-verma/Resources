from django.db import models

# Create your models here.

class Resource(models.Model):
    prompt = models.TextField(help_text="Enter the prompt text")
    articles = models.JSONField(
        default=list, 
        help_text="List of article URLs"
    )
    videos = models.JSONField(
        default=list, 
        help_text="List of video URLs"
    )

    def __str__(self):
        return self.prompt[:50]