from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):

    category_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.category_name

class Post(models.Model):

    created_at = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.CharField(max_length=200)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return str(self.id)

class Comment(models.Model):
    created_at = models.DateTimeField()
    comment_title = models.CharField(max_length=200)
    comment_content = models.TextField()
    comment_author = models.CharField(max_length=200)
    post = models.ForeignKey(Post)

    def set_values(self, *args, **kwargs):
        post = kwargs.pop('post')
        comment_content = kwargs.pop('comment_content')

        setattr(self, 'post', post)
        setattr(self, 'comment_title', comment_content[:80])
        setattr(self, 'created_at', datetime.now())

    def __unicode__(self):
        return self.comment_title


