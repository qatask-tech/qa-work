from django.db import models

class Service(models.Model):
    service_title = models.CharField(max_length=100)
    service_icon = models.CharField(max_length=50)  # e.g., Font Awesome icon classes
    service_desc = models.TextField()

    def __str__(self):
        return self.service_title
