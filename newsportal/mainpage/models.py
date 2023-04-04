from django.db import models

# Create your models here.

class News(models.Model):
    news_title = models.CharField(max_length=150)
    news_post = models.TextField()
    news_author = models.CharField(max_length=70)
    news_date = models.DateTimeField()

    def __str__(self):
        return self.news_title

class Supply_news(models.Model):
    supply_title = models.CharField(max_length=150)
    supply_post = models.TextField()
    supply_author = models.CharField(max_length=70)

    def __str__(self):
        return self.supply_title
