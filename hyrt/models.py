from django.db import models

class Letter(models.Model):
    sender = models.CharField(max_length=100, blank=True)
    recipient = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()


    def __str__(self):
        return self.recipient + ' ' + self.message