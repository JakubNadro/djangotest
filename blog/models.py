from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #ilość znaków w tytule
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def Publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  #wywołuje string zwracający tytuł
        return self.title


