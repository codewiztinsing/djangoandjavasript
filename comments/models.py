from django.db import models
from posts.models import Post

class Comment(models.Model):
    post    = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name    = models.CharField(max_length=80)
    email    = models.EmailField()
    body    = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} '.format(self.body)