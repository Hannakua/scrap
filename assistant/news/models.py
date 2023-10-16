from django.db import models


class Topic(models.Model):
    name = models.CharField()


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField()
    published_at = models.CharField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


