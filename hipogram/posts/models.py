from django.db import models
from hipogram.tags.models import Tag


class Post(models.Model):
    image = models.ImageField()
    text = models.TextField()
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    creation_datetime = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return f'{self.text} by {self.created_by.username}'
