from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class Post(models.Model):
    authour = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Task(models.Model):
    name = models.TextField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.done:
            return "%s (done)" % self.name
        else:
            return self.name


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_date = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

def approved_comments(self):
    return self.comments.filter(approved_comment=True)
