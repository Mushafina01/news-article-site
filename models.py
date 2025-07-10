from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
