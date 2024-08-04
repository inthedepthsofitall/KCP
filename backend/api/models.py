from django.db import models
import uuid
import random

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = uuid.uuid4().hex[:6]
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.original_url



